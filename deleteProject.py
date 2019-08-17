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
from informatica import manageFolder
import sys

now = datetime.datetime.now()
result = errorcodes.OK

def main(argv):
    thisproc = "MAIN"
    mainProc='deleteProject'

    resultlogger = supporting.configurelogger(mainProc)
    logger = logging.getLogger(mainProc)

    generalSettings.getenvvars()

    supporting.log(logger, logging.DEBUG, thisproc, 'Started')
    supporting.log(logger, logging.DEBUG, thisproc, 'logDir is >' + generalSettings.logDir + "<.")

    if len(argv) == 0:
        supporting.log(logger, logging.ERROR, thisproc, 'No project name specified.')
        result = errorcodes.INFACMD_NOPROJECT
        supporting.exitscript(resultlogger, result)

    project_name = argv[0]
    infaSettings.getinfaenvvars()
    infaSettings.outinfaenvvars()

    project = manageFolder.ManageFolder(Tool="DeleteProject",
                                        Domain=infaSettings.sourceDomain,
                                        ServiceName=infaSettings.sourceModelRepository,
                                        ProjectName=project_name,
                                        OnError=errorcodes.INFACMD_DELETE_PROJECT_FAILED
                                        )

    result = manageFolder.ManageFolder.manage(project)

    supporting.log(logger, logging.DEBUG, thisproc, 'Completed with return code >' + str(result.rc)
                   + '< and result code >' + result.code + "<.")
    supporting.exitscript(resultlogger, result)


main(sys.argv[1:])
