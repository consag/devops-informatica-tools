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
    parser.add_argument("-g", "--group", required=True, action="store", dest="group_name",
                        help="Name of the user group that needs to be created.")
    parser.add_argument("-d", "--description", required=False, action="store", dest="group_description",
                        help="The group description.")
    args = parser.parse_args()

    if args.group_description is None:
        args.group_description = "Created by createGroup.py on " + now.strftime('%Y-%m-%d %H:%M:%S.%f')

    return args


def main(argv):
    thisproc = "MAIN"
    mainProc = 'createGroup'

    resultlogger = supporting.configurelogger(mainProc)
    logger = logging.getLogger(mainProc)

    args = parse_the_arguments(argv)

    generalSettings.getenvvars()

    supporting.log(logger, logging.DEBUG, thisproc, 'Started')
    supporting.log(logger, logging.DEBUG, thisproc, 'logDir is >' + generalSettings.logDir + "<.")

    group_name = args.group_name
    group_description = args.group_description

    supporting.log(logger, logging.DEBUG, thisproc, 'Group name is >' + group_name + '<.')
    supporting.log(logger, logging.DEBUG, thisproc, 'Group description is >' + group_description + '<.')

    infaSettings.getinfaenvvars()
    infaSettings.outinfaenvvars()

    group = manageSecurity.ManageSecurity(Tool="CreateGroup",
                                          Domain=infaSettings.sourceDomain,
                                          GroupName=group_name,
                                          GroupDescription=group_description,
                                          OnError=errorcodes.INFACMD_CREATE_GROUP_FAILED
                                          )
    result = manageSecurity.ManageSecurity.manage(group)

    supporting.log(logger, logging.DEBUG, thisproc, 'Completed with return code >' + str(result.rc)
                   + '< and result code >' + result.code + "<.")
    supporting.exitscript(resultlogger, result)


if __name__ == '__main__':
    main(sys.argv[1:])
