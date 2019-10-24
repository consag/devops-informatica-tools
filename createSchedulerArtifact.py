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
# Create Scheduler Artifact
# @Since: 25-OCT-2019
# @Author: Jac. Beekers

import logging, datetime, supporting
import supporting.errorcodes as err
import scheduler.schedulerArtifactChecks as schedulerchecks
import scheduler.artifact
import scheduler.schedulerSettings as settings
import supporting.generalSettings as generalsettings
import sys, argparse

now = datetime.datetime.now()
result = err.OK


def parse_the_arguments(argv):
    """Parses the provided arguments and exits on an error.
    Use the option -h on the command line to get an overview of the required and optional arguments.
     """
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    return args


def main(argv):
    """Creates a Scheduler artifact, consisting of a list of schedule files, eg python code for Airflow or job-as-code JSON for bmc Control-M
    It uses a deploy list that contains subdirectories.
    Module uses environment variables that steer the artifact creation.
    """
    thisproc = "MAIN"
    mainProc = 'CreateSchedulerArtifact'

    resultlogger = supporting.configurelogger(mainProc)
    logger = logging.getLogger(mainProc)

    args = parse_the_arguments(argv)

    supporting.log(logger, logging.DEBUG, thisproc, 'Started')
    supporting.log(logger, logging.DEBUG, thisproc, 'logDir is >' + generalsettings.logDir + "<.")

    # Check requirements for artifact generation
    generalsettings.getenvvars()
    settings.getschedulerenvvars()
    settings.outschedulerenvvars()

    result = schedulerchecks.schedulerartifactchecks()
    if result.rc != 0:
        supporting.log(logger, logging.ERROR, thisproc,
                       'Scheduler Artifact Checks failed with >' + result.message + "<.")
        supporting.exitscript(resultlogger, result)

    result = scheduler.artifact.processList(settings.schedulerdeploylist)

    supporting.log(logger, logging.DEBUG, thisproc, 'Completed with return code >' + str(result.rc)
                   + '< and result code >' + result.code + "<.")
    #    supporting.writeresult(resultlogger, result)
    supporting.exitscript(resultlogger, result)


if __name__ == '__main__':
    main(sys.argv)
