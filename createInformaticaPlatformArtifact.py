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
# generalSettings
# @Since: 22-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190412.0 - JBE - Initial
##

import logging, datetime, supporting
import supporting.errorcodes as err
import informatica.infaArtifactChecks as infachecks
from informatica import artifact
import informatica.infaSettings as settings
import supporting.generalSettings as generalsettings
from informatica import infaConstants

now = datetime.datetime.now()
result = err.OK

def main():
    thisproc = "MAIN"
    mainProc='CreateDeveloperArtifact'

    resultlogger = supporting.configurelogger(mainProc)
    logger = logging.getLogger(mainProc)

    supporting.log(logger, logging.DEBUG, thisproc, 'Started')
    supporting.log(logger, logging.DEBUG, thisproc, 'logDir is >' + generalsettings.logDir + "<.")

    settings.getinfaenvvars()
    settings.outinfaenvvars()

    # Check requirements for artifact generation
    result = infachecks.infaartifactchecks()
    if result.rc != 0:
        supporting.log(logger, logging.ERROR, thisproc, 'INFA Checks failed with >' + result.message +"<.")
        supporting.exitscript(resultlogger, result)

    result = artifact.processList(infaConstants.CREATEARTIFACT, settings.infadeploylist)

    supporting.log(logger, logging.DEBUG, thisproc, 'Completed with return code >' + str(result.rc)
                   + '< and result code >' + result.code + "<.")
#    supporting.writeresult(resultlogger, result)
    supporting.exitscript(resultlogger, result)


main()
