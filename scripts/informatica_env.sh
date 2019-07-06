##
#
curDir="$(dirname "$(readlink -f "$0")")"

##
# set JAVA environment
. ${curDir}/java_env.sh
##
# set Oracle environment
. ${curDir}/oracle_env.sh
##
# set security environment
. ${curDir}/security_env.sh

##
# Informatica
INFA_VERSION=10.2.0
export INFA_VERSION
INFA_HOME=/appl/Informatica/$INFA_VERSION
export INFA_HOME

##
# ODBC
ODBCINI=${curDir}/odbc.ini
export ODBCINI
ODBCINSTINI=${curDir}/odbcinst.ini
export ODBCINSTINI

##
# PATHs: Informatica first
LD_LIBRARY_PATH=${INFA_HOME}/server/bin:${INFA_HOME}/ODBC7.1/lib:${INFA_HOME}/services/shared/bin:${INFA_HOME}/isp/bin:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH
PATH=${INFA_HOME}/server/bin:${INFA_HOME}/tomcat/bin:${INFA_HOME}/isp/bin:$PATH
export PATH



