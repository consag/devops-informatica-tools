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

#  MIT License
#
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#
#

import logging, datetime, supporting
from supporting import errorcodes
from cicd.informatica import infaSettings, jobManagement
from supporting import generalSettings
import sys
import argparse

now = datetime.datetime.now()
result = errorcodes.OK


class ExecuteInformaticaMapping:
    """
        Runs an Informatica Mapping
    """

    def __init__(self, argv):
        self.argv = argv

    def parse_the_arguments(self):
        """Parses the provided arguments and exits on an error.
        Use the option -h on the command line to get an overview of the required and optional arguments.
         """
        parser = argparse.ArgumentParser()
        parser.add_argument("-a", "--application", required=True, action="store", dest="application_name",
                            help="Application that contains the object to run.")
        parser.add_argument("-m", "--mapping", help="Mapping to run.", required=True, action="store",
                            dest="mapping_name")
        parser.add_argument("-p", "--pushdown", help="Database push-down type", action="store", dest="pushdown_type"
                            , choices=["Source", "Target", "Full"], default="Source")
        parser.add_argument("-o", "--optimizationlevel", action="store", dest="optimization_level"
                            , default="3", help="Optimization level to apply", choices=["0", "1", "2", "3", "4", "5"])
        parser.add_argument("-l", "--loglevel", type=int, action="store", dest="loglevel", choices=[0, 1, 2, 3, 4, 5]
                            , help="log level from 0=fatal to 5=verbose")
        parser.add_argument("-x", "-extra", action="store", dest="as_is_options",
                            help="any options to add. Make sure to use double-quotes!")
        args = parser.parse_args()

        if args.as_is_options is None:
            args.as_is_options = ""

        return args

    def runit(self):
        """Runs a Mapping.
        usage: runMapping.py [-h] -a APPLICATION_NAME -m MAPPING_NAME
                     [-p {Source,Target,Full}] [-o {0,1,2,3,4,5}]
                     [-l {0,1,2,3,4,5}] [-x AS_IS_OPTIONS]
        """
        thisproc = "MAIN"
        mainProc = 'runMapping'

        args = ExecuteInformaticaMapping.parse_the_arguments(self)

        resultlogger = supporting.configurelogger(mainProc)
        logger = logging.getLogger(mainProc)

        generalSettings.getenvvars()

        supporting.log(logger, logging.DEBUG, thisproc, 'Started')
        supporting.log(logger, logging.DEBUG, thisproc, 'logDir is >' + generalSettings.logDir + "<.")

        application_name = args.application_name
        mapping_name = args.mapping_name

        pushdown_type = args.pushdown_type
        optimization_level = args.optimization_level
        as_is_options = args.as_is_options

        infaSettings.getinfaenvvars()
        infaSettings.outinfaenvvars()
        supporting.logentireenv()

        """with AsIsOptions, you can speficy e.g. a parameter set
            Example:
            runMapping myApp myMapping Source 3 "-ParameterSet myParameterSet -OperatingSystemProfile myOSProfile"
            It is important to supply the AsIsOptions as one single string
        """
        mapping = jobManagement.JobExecution(Tool="RunMapping",
                                             Domain=infaSettings.sourceDomain,
                                             ServiceName=infaSettings.sourceDIS,
                                             Application=application_name,
                                             Mapping=mapping_name,
                                             PushdownType=pushdown_type,
                                             OptimizationLevel=optimization_level,
                                             Wait="true",
                                             OnError=errorcodes.INFACMD_MAPPING_FAILED,
                                             AsIsOptions=as_is_options
                                             )
        result = jobManagement.JobExecution.manage(mapping)

        supporting.log(logger, logging.DEBUG, thisproc, 'Completed with return code >' + str(result.rc)
                       + '< and result code >' + result.code + "<.")
        supporting.exitscript(resultlogger, result)


if __name__ == '__main__':
    infa = ExecuteInformaticaMapping(sys.argv[1:])
    infa.runit()
