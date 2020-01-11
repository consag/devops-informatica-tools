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
from cicd.informatica import manageSecurity
import sys, argparse

now = datetime.datetime.now()
result = errorcodes.OK


def parse_the_arguments(argv):
    """Parses the provided arguments and exits on an error.
    Use the option -h on the command line to get an overview of the required and optional arguments.
     """
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--outputfile", required=True, action="store", dest="output_file",
                        help="File to export the users and groups to. Tip: Include the path.")
    parser.add_argument("-f", "--force", required=False, action="store", dest="force",
                        choices=["false", "true"],
                        help="If the target file exists it will be overwritten (true) or not (false). Default is >false<.")
    parser.add_argument("-r", "--retainpassword", required=False, action="store", dest="retain_password",
                        choices=["false", "true"],
                        help="Determines if the user passwords should be exported (true) or not (false). Default is >true<.")
    args = parser.parse_args()

    if args.force is None:
        args.force = "false"

    if args.retain_password is None:
        args.retain_password = "true"

    return args


def main(argv):
    """Exports users and groups.
    usage: exportUsersAndGroups.py [-h] -o OUTPUT_FILE [-f {false,true}]
                               [-r {false,true}]
    where:
    -f or --force: Overwrite output file if it exists
    -r or --retainpassword: If set to "false" user passwords are not exported. If "true" they will be.
    """
    thisproc = "MAIN"
    mainProc = 'exportUsersAndGroups'

    resultlogger = supporting.configurelogger(mainProc)
    logger = logging.getLogger(mainProc)

    args = parse_the_arguments(argv)

    generalSettings.getenvvars()

    supporting.log(logger, logging.DEBUG, thisproc, 'Started')
    supporting.log(logger, logging.DEBUG, thisproc, 'logDir is >' + generalSettings.logDir + "<.")

    export_file_name = args.output_file
    force = args.force
    retain_password = args.retain_password

    infaSettings.getinfaenvvars()
    infaSettings.outinfaenvvars()

    users_and_groups = manageSecurity.ManageSecurity(Tool="ExportUsersAndGroups",
                                                     Domain=infaSettings.sourceDomain,
                                                     ExportFile=export_file_name,
                                                     Force=force,
                                                     RetainPassword=retain_password,
                                                     OnError=errorcodes.INFACMD_EXPORT_USRGRP_FAILED
                                                     )

    result = manageSecurity.ManageSecurity.manage(users_and_groups)

    supporting.log(logger, logging.DEBUG, thisproc, 'Completed with return code >' + str(result.rc)
                   + '< and result code >' + result.code + "<.")
    supporting.exitscript(resultlogger, result)


if __name__ == '__main__':
    main(sys.argv[1:])
