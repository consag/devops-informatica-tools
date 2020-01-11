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
from cicd.informatica import infaSettings
from supporting import generalSettings
from cicd.informatica import manageFolder
import sys, argparse

now = datetime.datetime.now()
result = errorcodes.OK


def parse_the_arguments(argv):
    """Parses the provided arguments and exits on an error.
    Use the option -h on the command line to get an overview of the required and optional arguments.
     """
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--project", required=True, action="store", dest="project_name",
                        help="Project the folder should be removed from.")
    parser.add_argument("-f", "--folder", required=True, action="store", dest="folder_name",
                        help="Name of the folder to be deleted.")
    args = parser.parse_args()

    return args


def main(argv):
    """Removes a folder from a project
    Usage: deleteFolder.py [-h] -p PROJECT_NAME -f FOLDER_NAME
    """
    thisproc = "MAIN"
    mainProc = 'deleteFolder'

    resultlogger = supporting.configurelogger(mainProc)
    logger = logging.getLogger(mainProc)

    args = parse_the_arguments(argv)

    generalSettings.getenvvars()

    supporting.log(logger, logging.DEBUG, thisproc, 'Started')
    supporting.log(logger, logging.DEBUG, thisproc, 'logDir is >' + generalSettings.logDir + "<.")

    project_name = args.project_name
    folder_name = args.folder_name

    infaSettings.getinfaenvvars()
    infaSettings.outinfaenvvars()

    folder = manageFolder.ManageFolder(Tool="DeleteFolder",
                                       Domain=infaSettings.sourceDomain,
                                       ServiceName=infaSettings.sourceModelRepository,
                                       ProjectName=project_name,
                                       Path=folder_name,
                                       OnError=errorcodes.INFACMD_DELETE_FOLDER_FAILED
                                       )
    result = manageFolder.ManageFolder.manage(folder)

    supporting.log(logger, logging.DEBUG, thisproc, 'Completed with return code >' + str(result.rc)
                   + '< and result code >' + result.code + "<.")
    supporting.exitscript(resultlogger, result)


if __name__ == '__main__':
    main(sys.argv[1:])
