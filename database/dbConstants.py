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
# Constants for Database artifacts and deploys
# @Since: 22-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190410.0 - JBE - Initial
# @Version: 20190817.0 - JBE - Added user/password functionality

# Database artifacts
varOracleSchemaName='ORACLE_SCHEMA'
varOracleDeployList='ORACLE_DEPLOYLIST'
varSourceSqlDir='SOURCE_SQLDIR'
varTargetSqlDir='TARGET_SQLDIR'
varSqlPrefix = 'SQL_PREFIX'
varOracleDatabaseUser = 'ORACLE_USER'
varDatabaseUserPassword = 'ORACLE_PASSWORD' # encrypted
varOracleTNSName = 'ORACLE_TNS'

##
# Database artifact defaults
DEFAULT_SOURCE_SQLDIR ='.'
DEFAULT_TARGET_SQLDIR ='.'
DEFAULT_ORACLE_DEPLOYLIST ='oracle_deploylist.txt'
DEFAULT_SQL_DEPLOYLIST ='sqlserver_deploylist.txt'
DEFAULT_DB2_DEPLOYLIST ='db2_deploylist.txt'
DEFAULT_SQL_PREFIX = ''

NOT_SET ='NOT_SET'
