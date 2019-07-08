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
# dbSettings
# @Since: 22-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190410.0 - JBE - Initial
##

import database.dbConstants as constants
import supporting, os, logging
import supporting.generalSettings as generalsettings
from supporting.generalSettings import completePath

logger = logging.getLogger(__name__)

sourcesqldir = constants.DEFAULT_SOURCE_SQLDIR
targetsqldir = constants.DEFAULT_TARGET_SQLDIR
databaseType = 'UNKNOWN'
sqlprefix = constants.DEFAULT_SQL_PREFIX

def getdbenvvars():
    thisproc="getdbenvvars"
    global dbdeploylist, sourcesqldir, targetsqldir, sqlprefix
    supporting.log(logger, logging.DEBUG, thisproc, 'started')
    dbdeploylist = completePath(os.environ.get(constants.varOracleDeployList, constants.DEFAULT_ORACLE_DEPLOYLIST), generalsettings.sourceDir)
    sourcesqldir = completePath(os.environ.get(constants.varSourceSqlDir, constants.DEFAULT_SOURCE_SQLDIR), generalsettings.sourceDir)
    targetsqldir = completePath(os.environ.get(constants.varTargetSqlDir, constants.DEFAULT_TARGET_SQLDIR), generalsettings.sourceDir)
    # prefix for ordered sql files
    sqlprefix = os.environ.get(constants.varSqlPrefix, constants.DEFAULT_SQL_PREFIX)

    supporting.log(logger, logging.DEBUG, thisproc, 'completed')


def outdbenvvars():
    thisproc = "outdbenvvars"
    supporting.log(logger, logging.DEBUG, thisproc, 'started')
    supporting.log(logger, logging.INFO, thisproc, 'dbdeploylist is >' + dbdeploylist + "<.")
    supporting.log(logger, logging.INFO, thisproc, 'sourcesqldir is >' + sourcesqldir +"<.")
    supporting.log(logger, logging.INFO, thisproc, 'targetsqldir is >' + targetsqldir +"<.")
    supporting.log(logger, logging.DEBUG, thisproc, 'completed')
