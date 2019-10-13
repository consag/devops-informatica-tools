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
from informatica import infaSettings
from supporting import generalSettings
from informatica import jobManagement
import sys
import argparse

now = datetime.datetime.now()
result = errorcodes.OK

def parse_the_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--profile", required=True, action="store", dest="object_path",
                        help="Profile, including path, to run.")
    args = parser.parse_args()

    return args

def main(argv):
    thisproc = "MAIN"
    mainProc='runProfile'

    resultlogger = supporting.configurelogger(mainProc)
    logger = logging.getLogger(mainProc)

    generalSettings.getenvvars()

    supporting.log(logger, logging.DEBUG, thisproc, 'Started')
    supporting.log(logger, logging.DEBUG, thisproc, 'logDir is >' + generalSettings.logDir + "<.")

    args = parse_the_arguments(argv)
    objectPath = args.object_path
    infaSettings.getinfaenvvars()
    infaSettings.outinfaenvvars()
    supporting.logentireenv()

    profile = jobManagement.JobExecution(Tool="RunProfile",
                                         Domain=infaSettings.sourceDomain,
                                         MrsServiceName=infaSettings.sourceModelRepository,
                                         DsServiceName=infaSettings.sourceDIS,
                                         ObjectPathAndName=objectPath,
                                         ObjectType="profile",
                                         Wait="true",
                                         OnError=errorcodes.INFACMD_PROFILE_FAILED
                                         )
    result = jobManagement.JobExecution.manage(profile)

    supporting.log(logger, logging.DEBUG, thisproc, 'Completed with return code >' + str(result.rc)
                   + '< and result code >' + result.code + "<.")
    supporting.exitscript(resultlogger, result)


main(sys.argv[1:])
