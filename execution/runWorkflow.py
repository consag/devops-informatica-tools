#  MIT License
#
#  Copyright (c) 2019 Jac. Beekers
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#

import logging, datetime, supporting
from supporting import errorcodes
from cicd.informatica import infaSettings, jobManagement
from supporting import generalSettings
import sys
import argparse

now = datetime.datetime.now()
result = errorcodes.OK


class ExecuteInformaticaWorkflow:
    """
        Runs an Informatica Workflow
    """

    def __init__(self, argv, log_on_console=True):
        self.arguments = argv
        self.mainProc = 'runWorkflow'
        self.resultlogger = supporting.configurelogger(self.mainProc, log_on_console)
        self.logger = supporting.logger

    def parse_the_arguments(self, arguments):
        """Parses the provided arguments and exits on an error.
        Use the option -h on the command line to get an overview of the required and optional arguments.
        """
        parser = argparse.ArgumentParser(prog='runWorkflow')

        parser.add_argument("-a", "--application", required=True, action="store", dest="application_name",
                            help="Application that contains the object to run.")
        parser.add_argument("-w", "--workflow", help="Workflow to run.", required=True, action="store",
                            dest="workflow_name")
        parser.add_argument("-c", "--completion", help="Wait for workflow completion", action="store", dest="wait"
                            , choices=["True", "False"], default="False")
        parser.add_argument("-f", "--osprofile", action="store", dest="os_profile",
                            help="Informatica OSProfile to use.")
        parser.add_argument("-x", "-extra", action="store", dest="as_is_options",
                            help="any options to add. Make sure to use double-quotes!")
        args = parser.parse_args(arguments)

        if args.as_is_options is None:
            args.as_is_options = ""

        return args

    def runit(self, arguments):
        """Runs a Workflow.
        usage: runWorkflow.py [-h] -a APPLICATION_NAME -w WORKFLOW_NAME
                          [-c {True,False}] [-x AS_IS_OPTIONS]
        with AsIsOptions, you can speficy e.g. a parameter set
            Example:
            runMapping myApp myMapping Source 3 "-ParameterSet myParameterSet -OperatingSystemProfile myOSProfile"
            It is important to supply the AsIsOptions as one single string
        """
        thisproc = "runit"

        args = self.parse_the_arguments(arguments)

        generalSettings.getenvvars()

        supporting.log(self.logger, logging.DEBUG, thisproc, 'Started')
        supporting.log(self.logger, logging.DEBUG, thisproc, 'logDir is >' + generalSettings.logDir + "<.")

        application_name = args.application_name
        workflow_name = args.workflow_name
        wait = args.wait
        as_is_options = args.as_is_options
        os_profile = args.os_profile

        infaSettings.getinfaenvvars()
        infaSettings.outinfaenvvars()
        #        supporting.logentireenv()

        workflow = jobManagement.JobExecution(Tool="RunWorkflow",
                                              # this will translate to StartWorkflow for the infacmd
                                              Domain=infaSettings.sourceDomain,
                                              ServiceName=infaSettings.sourceDIS,
                                              Application=application_name,
                                              Workflow=workflow_name,
                                              Wait=wait,
                                              OnError=errorcodes.INFACMD_WORKFLOW_FAILED,
                                              OperatingSystemProfile=os_profile,
                                              AsIsOptions=as_is_options
                                              )
        result = jobManagement.JobExecution.manage(workflow)

        supporting.log(self.logger, logging.DEBUG, thisproc, 'Completed with return code >' + str(result.rc)
                       + '< and result code >' + result.code + "<.")
        return result


if __name__ == '__main__':
    infa = ExecuteInformaticaWorkflow(sys.argv[1:], log_on_console=True)
    result = infa.runit(infa.arguments)
    supporting.exitscript(infa.resultlogger, result)
