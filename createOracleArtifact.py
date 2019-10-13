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
# Create Oracle Database Artifact
# @Since: 22-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190414.0 - JBE - Initial

import logging, datetime, supporting
import supporting.errorcodes as err
import database.databaseArtifactChecks as dbchecks
import database.artifact
import database.dbSettings as settings
import supporting.generalSettings as generalsettings

now = datetime.datetime.now()
result = err.OK
settings.databaseType = 'Oracle'


def main():
    thisproc = "MAIN"
    mainProc = 'CreateOracleArtifact'

    resultlogger = supporting.configurelogger(mainProc)
    logger = logging.getLogger(mainProc)

    supporting.log(logger, logging.DEBUG, thisproc, 'Started')
    supporting.log(logger, logging.DEBUG, thisproc, 'logDir is >' + generalsettings.logDir + "<.")

    # Check requirements for artifact generation
    generalsettings.getenvvars()
    settings.getdbenvvars()
    settings.outdbenvvars()

    result = dbchecks.databaseartifactchecks()
    if result.rc != 0:
        supporting.log(logger, logging.ERROR, thisproc,
                       'Database Artifact Checks failed with >' + result.message + "<.")
        supporting.exitscript(resultlogger, result)

    result = database.artifact.processList(settings.dbdeploylist)

    supporting.log(logger, logging.DEBUG, thisproc, 'Completed with return code >' + str(result.rc)
                   + '< and result code >' + result.code + "<.")
    #    supporting.writeresult(resultlogger, result)
    supporting.exitscript(resultlogger, result)


if __name__ == '__main__':
    main()
