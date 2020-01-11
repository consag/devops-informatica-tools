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
# @Version: 20190817.0 - JBE - Added user/password functionality
##

import cicd.database.dbConstants as constants
import supporting, os, logging
import supporting.generalSettings as generalsettings
from supporting.generalSettings import completePath

logger = logging.getLogger(__name__)

sourcesqldir = constants.DEFAULT_SOURCE_SQLDIR
targetsqldir = constants.DEFAULT_TARGET_SQLDIR
databaseType = 'UNKNOWN'
sqlprefix = constants.DEFAULT_SQL_PREFIX
if os.name == 'nt':
    sqlplus_command = 'sqlplus.exe'
else:
    sqlplus_command = 'sqlplus'

def getdbenvvars():
    thisproc="getdbenvvars"
    global dbdeploylist, sourcesqldir, targetsqldir, sqlprefix
    supporting.log(logger, logging.DEBUG, thisproc, 'started')
    dbdeploylist = completePath(os.environ.get(constants.varOracleDeployList, constants.DEFAULT_ORACLE_DEPLOYLIST), generalsettings.sourceDir)
    sourcesqldir = completePath(os.environ.get(constants.varSourceSqlDir, constants.DEFAULT_SOURCE_SQLDIR), generalsettings.sourceDir)
    targetsqldir = completePath(os.environ.get(constants.varTargetSqlDir, constants.DEFAULT_TARGET_SQLDIR), generalsettings.sourceDir)
    # prefix for ordered sql files
    sqlprefix = os.environ.get(constants.varSqlPrefix, constants.DEFAULT_SQL_PREFIX)


def getschemaenvvars(schema):
    thisproc="getschemaenvvars"
    global database_user, database_schema, database_user_password, database_tns_name
    # Database user etc.
    database_user = os.environ.get(constants.varOracleDatabaseUser + "_" + schema, constants.NOT_SET)
    database_user_password = os.environ.get(constants.varDatabaseUserPassword + "_" + schema, constants.NOT_SET)
    database_schema = os.environ.get(constants.varOracleSchemaName + "_" + schema, constants.NOT_SET)
    database_tns_name = os.environ.get(constants.varOracleTNSName + "_" + schema, constants.NOT_SET)

    supporting.log(logger, logging.DEBUG, thisproc, 'completed')
    return database_tns_name, database_schema, database_user, database_user_password


def outdbenvvars():
    thisproc = "outdbenvvars"
    supporting.log(logger, logging.INFO,  thisproc, 'dbdeploylist is >' + dbdeploylist + "<.")
    supporting.log(logger, logging.INFO,  thisproc, 'sourcesqldir is >' + sourcesqldir +"<.")
    supporting.log(logger, logging.INFO,  thisproc, 'targetsqldir is >' + targetsqldir +"<.")


def outschemaenvvars():
    thisproc = "outdbenvvars"
    supporting.log(logger, logging.DEBUG, thisproc, 'database_tns_name is >' + database_tns_name +"<.")
    supporting.log(logger, logging.DEBUG, thisproc, 'database_schema is >' + database_schema +"<.")
    supporting.log(logger, logging.DEBUG, thisproc, 'database user is >' + database_user +"<.")
    if database_user_password is None:
        supporting.log(logger, logging.WARNING, thisproc, 'database_user_password is empty')
    else:
        supporting.log(logger, logging.DEBUG, thisproc, 'database_user_password has been determined.')

