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
from supporting.randomize import randomStringDigits

now = datetime.datetime.now()
result = errorcodes.OK


def parse_the_arguments(argv):
    """Parses the provided arguments and exits on an error.
    Use the option -h on the command line to get an overview of the required and optional arguments.
     """
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", required=True, action="store", dest="username",
                        help="User to be created.")
    parser.add_argument("-p", "--password", required=False, action="store", dest="password",
                        help="User password. If not provided a password will be generated.")
    parser.add_argument("-f", "--fullname", required=True, action="store", dest="fullname",
                        help="User full name.")
    parser.add_argument("-d", "--description", required=False, action="store", dest="description",
                        help="A description for the user. If not provided, the description will be generated with the creation timestamp.")
    parser.add_argument("-e", "--email", required=False, action="store", dest="email",
                        help="The email address of the user.")
    parser.add_argument("-n", "--phone", required=False, action="store", dest="phonenumber",
                        help="The user's phone number.")
    args = parser.parse_args()

    if args.password is None:
        args.password = randomStringDigits(12)
        generated_password = True
    else:
        generated_password = False

    if args.description is None:
        args.description = "Created by createUser.py on " + now.strftime('%Y-%m-%d %H:%M:%S.%f')
    if args.email is None:
        args.email = ""
    if args.phonenumber is None:
        args.phonenumber = ""

    return args, generated_password


def main(argv):
    """Create a user.
    If a password is not provided, one will be generated
    usage: createUser.py [-h] -u USERNAME [-p PASSWORD] -f FULLNAME
                     [-d DESCRIPTION] [-e EMAIL] [-n PHONENUMBER]
    """
    thisproc = "MAIN"
    mainProc = 'createUser'

    resultlogger = supporting.configurelogger(mainProc)
    logger = logging.getLogger(mainProc)

    args, generated_password = parse_the_arguments(argv)

    generalSettings.getenvvars()

    supporting.log(logger, logging.DEBUG, thisproc, 'Started')
    supporting.log(logger, logging.DEBUG, thisproc, 'logDir is >' + generalSettings.logDir + "<.")

    user_name = args.username
    user_password = args.password
    user_fullname = args.fullname
    user_description = args.description
    user_email = args.email
    user_phone = args.phonenumber

    if generated_password:
        print(args.password)

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
