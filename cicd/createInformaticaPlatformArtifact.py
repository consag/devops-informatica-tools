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

##
# generalSettings
# @Since: 22-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190412.0 - JBE - Initial
##

import logging, datetime, supporting
import supporting.errorcodes as err
import cicd.informatica.infaArtifactChecks as infachecks
from cicd.informatica import artifact
from cicd.informatica import infaSettings as settings
import supporting.generalSettings as generalsettings
from cicd.informatica import infaConstants
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
    """Generate an Informatica Platform artifact based on environment variables
    """
    thisproc = "MAIN"
    mainProc = 'CreateInformaticaPlatformArtifact'

    resultlogger = supporting.configurelogger(mainProc)
    logger = logging.getLogger(mainProc)

    args = parse_the_arguments(argv)

    supporting.log(logger, logging.DEBUG, thisproc, 'Started')
    supporting.log(logger, logging.DEBUG, thisproc, 'logDir is >' + generalsettings.logDir + "<.")

    settings.getinfaenvvars()
    settings.outinfaenvvars()

    # Check requirements for artifact generation
    # if there is no deploylist, then ignore building the artifact
    result = infachecks.infaartifactchecks()
    if result.rc == err.IGNORE.rc:
        # deploylist is not mandatory since 2020-02-09
        supporting.log(logging, result.level, thisproc, 'Artifact ignored.')
        result = err.OK
    else:
        if result.rc != 0:
            supporting.log(logger, logging.ERROR, thisproc,
                           'Informatica Platform Artifact Checks failed with >' + result.message + "<.")
            supporting.exitscript(resultlogger, result)
        else:
            result = artifact.processList(infaConstants.CREATEARTIFACT, settings.infadeploylist)

    supporting.log(logger, logging.DEBUG, thisproc, 'Completed with return code >' + str(result.rc)
                   + '< and result code >' + result.code + "<.")
    #    supporting.writeresult(resultlogger, result)
    supporting.exitscript(resultlogger, result)


if __name__ == '__main__':
    main(sys.argv)
