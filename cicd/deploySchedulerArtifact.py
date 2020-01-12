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

##
# Deploy Scheduler Artifact
# @Since: 12-JAN-2020
# @Author: Jac. Beekers

import logging, datetime, supporting
import supporting.errorcodes as err
from cicd.scheduler import schedulerArtifactChecks as schedulerChecks
from cicd.scheduler import schedulerSettings as settings
from cicd.scheduler import artifact as artifact
#from cicd.scheduler import schedulerConstants as constants
import supporting.generalSettings as generalSettings
import sys, argparse

now = datetime.datetime.now()
result = err.OK


class DeploySchedulerArtifact:
    """
        Deploys an artifact with Schedules
    """

    def __init__(self, argv, log_on_console=True):
        self.arguments = argv
        self.mainProc = 'deploySchedulerArtifact'
        self.resultlogger = supporting.configurelogger(self.mainProc, log_on_console)
        self.logger = supporting.logger

    def parse_the_arguments(self, arguments):
        """Parses the provided arguments and exits on an error.
        Use the option -h on the command line to get an overview of the required and optional arguments.
        """
        parser = argparse.ArgumentParser(prog='deploySchedulerArtifact')
        args = parser.parse_args(arguments)

        return args

    def runit(self, arguments):
        """Deploys a scheduler artifact.
        """
        thisproc = "runit"

        args = self.parse_the_arguments(arguments)

        generalSettings.getenvvars()

        supporting.log(self.logger, logging.DEBUG, thisproc, 'DUMMY DUMMY Started')
        supporting.log(self.logger, logging.DEBUG, thisproc, 'logDir is >' + generalSettings.logDir + "<.")

        # Check requirements for artifact generation
        generalSettings.getenvvars()
        settings.getschedulerenvvars()
        settings.outschedulerenvvars()

        result = schedulerChecks.schedulerartifactchecks()
        if result.rc != 0:
            supporting.log(self.logger, logging.ERROR, thisproc,
                           'Scheduler Artifact Checks failed with >' + result.message + "<.")
            supporting.exitscript(self.resultlogger, result)

#        result = artifact.processList(settings.schedulerdeploylist)

        supporting.log(self.logger, logging.DEBUG, thisproc, 'Completed with return code >' + str(result.rc)
                       + '< and result code >' + result.code + "<.")
        #    supporting.writeresult(resultlogger, result)
        return result


if __name__ == '__main__':
    deploy_artifact = DeploySchedulerArtifact(sys.argv[1:], log_on_console=True)
    result = deploy_artifact.runit(deploy_artifact.arguments)
    supporting.exitscript(deploy_artifact.resultlogger, result)
