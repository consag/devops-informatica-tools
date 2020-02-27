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
from cicd.informatica import infaSettings, jobManagement
from supporting import generalSettings
import sys
import argparse

now = datetime.datetime.now()
result = errorcodes.OK


class ExecuteInformaticaProfile:
    """
        Runs an Informatica Profile
    """

    def __init__(self, argv, log_on_console=True):
        self.arguments = argv
        self.mainProc = 'runProfile'
        self.resultlogger = supporting.configurelogger(self.mainProc, log_on_console)
        self.logger = supporting.logger

    def parse_the_arguments(self, arguments):
        """Parses the provided arguments and exits on an error.
        Use the option -h on the command line to get an overview of the required and optional arguments.
        """

        parser = argparse.ArgumentParser(prog='runProfile')
        parser.add_argument("-p", "--profile", required=True, action="store", dest="object_path",
                            help="Profile, including path, to run.")
        parser.add_argument("-f", "--osprofile", action="store", dest="os_profile",
                            help="Informatica OSProfile to use.")
        parser.add_argument("-x", "--extra", action="store", dest="as_is_options",
                            help="any options to add. Make sure to use double-quotes!")

        args = parser.parse_args(arguments)

        return args

    def runit(self, arguments):
        """Runs a Profile.
        usage: runProfile.py [-h] -p OBJECT_PATH
        """
        thisproc = "runit"
        args = self.parse_the_arguments(arguments)

        generalSettings.getenvvars()

        supporting.log(self.logger, logging.DEBUG, thisproc, 'Started')
        supporting.log(self.logger, logging.DEBUG, thisproc, 'logDir is >' + generalSettings.logDir + "<.")

        object_path = args.object_path
        os_profile = args.os_profile
        as_is_options = args.as_is_options

        infaSettings.getinfaenvvars()
        infaSettings.outinfaenvvars()

        profile = jobManagement.JobExecution(Tool="RunProfile",
                                             Domain=infaSettings.sourceDomain,
                                             MrsServiceName=infaSettings.sourceModelRepository,
                                             DsServiceName=infaSettings.sourceDIS,
                                             ObjectPathAndName=object_path,
                                             ObjectType="profile",
                                             Wait="true",
                                             OnError=errorcodes.INFACMD_PROFILE_FAILED,
                                             OperatingSystemProfile=os_profile,
                                             AsIsOptions=as_is_options
                                             )
        result = jobManagement.JobExecution.manage(profile)

        supporting.log(self.logger, logging.DEBUG, thisproc, 'Completed with return code >' + str(result.rc)
                       + '< and result code >' + result.code + "<.")
        return result


if __name__ == '__main__':
    infa = ExecuteInformaticaProfile(sys.argv[1:], log_on_console=True)
    result = infa.runit(infa.arguments)
    supporting.exitscript(infa.resultlogger, result)
