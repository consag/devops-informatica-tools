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
from informatica import manageSecurity
import sys

now = datetime.datetime.now()
result = errorcodes.OK


def main(argv):
    thisproc = "MAIN"
    mainProc = 'createUser'

    resultlogger = supporting.configurelogger(mainProc)
    logger = logging.getLogger(mainProc)

    generalSettings.getenvvars()

    supporting.log(logger, logging.DEBUG, thisproc, 'Started')
    supporting.log(logger, logging.DEBUG, thisproc, 'logDir is >' + generalSettings.logDir + "<.")

    if len(argv) < 3:
        supporting.log(logger, logging.ERROR, thisproc, 'No user name, password and/or full name specified.')
        result = errorcodes.INFACMD_NOUSERNAME
        supporting.exitscript(resultlogger, result)

    # mandatory
    user_name = argv[0]
    user_password = argv[1]
    user_fullname = argv[2]
    # optional
    user_description = argv[3] if len(argv) > 3 else ""
    user_email = argv[4] if len(argv) > 4 else ""
    user_phone = argv[5] if len(argv) > 5 else ""

    infaSettings.getinfaenvvars()
    infaSettings.outinfaenvvars()

    user = manageSecurity.ManageSecurity(Tool="CreateUser",
                                         Domain=infaSettings.sourceDomain,
                                         NewUserName=user_name,
                                         NewUserPassword=user_password,
                                         NewUserFullName=user_fullname,
                                         NewUserDescription=user_description,
                                         NewUserEmailAddress=user_email,
                                         NewUserPhoneNumber=user_phone,
                                         OnError=errorcodes.INFACMD_CREATE_USER_FAILED
                                         )
    result = manageSecurity.ManageSecurity.manage(user)

    supporting.log(logger, logging.DEBUG, thisproc, 'Completed with return code >' + str(result.rc)
                   + '< and result code >' + result.code + "<.")
    supporting.exitscript(resultlogger, result)


if __name__ == '__main__':
    main(sys.argv[1:])
