##
# Constants
# @Since: 22-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190324.0 - JBE - Initial

##
# Environment variable values
##
# Generic
varLogDir='LOGDIR'
varResultDir='RESULTDIR'
# Database artifacts
varOracleSchemaName='ORACLE_SCHEMANAME'
varOracleDeployList='ORACLE_DEPLOYLIST'
varSourceSqlDir='ORACLE_SOURCE_SQLDIR'
varTargetSqlDir='ORACLE_TARGET_SQLDIR'
# Informatica artifacts
varOracleDeployList='INFA_DEPLOYLIST'

##
#
##
NOT_SET = 'NotSet'

##
# Environment defaults
#If not set on command line (if supported) and not as environment variable
DEFAULT_LOGDIR ='.'
##
# Database artifact defaults
DEFAULT_SOURCE_SQLDIR ='.'
DEFAULT_TARGET_SQLDIR ='.'
DEFAULT_ORACLE_DEPLOYLIST ='oracle_deploylist.txt'
DEFAULT_SQL_DEPLOYLIST ='sqlserver_deploylist.txt'
DEFAULT_DB2_DEPLOYLIST ='db2_deploylist.txt'

##
# Informatica
DEFAULT_DEVELOPER_DEPLOYLIST ='developer_deploylist.txt'
DEFAULT_POWERCENTER_DEPLOYLIST ='powercenter_deploylist.txt'

##
# Resources: parameter. sql, etc
DEFAULT_RESOURCE_DEPLOYLIST ='resources_deploylist.txt'

##
# Airflow
DEFAULT_DAG_DEPLOYLIST ='dag_deploylist.txt'
