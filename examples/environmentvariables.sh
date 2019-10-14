environmentDir=/data/environment
scriptDir=${environmentDir}/scripts
cd ${scriptDir}
##
# additional environment settings may be needed.
# Configure environment so modules can use the Oracle client
. ./oracle_env.sh
# Configure environment so modules can use the Informatica client
. ./informatica_env.sh
# Configure environment so modules are executed in the correct python venv
. ./python_env.sh
##
# Taken from python_env
cd $devopstoolsDir
##
# general
LOGDIR=/data/logs/scheduler
if [ ! -d $LOGDIR ] ; then
        mkdir $LOGDIR
fi
##
# Where result output files should be created
RESULTDIR=/data/logs/results
if [ ! -d $RESULTDIR ] ; then
        mkdir $RESULTDIR
fi
#CONFIGDIR=
##
# informatica infacmd connectivity info
SOURCE_INFACMD_LOCATION=${INFA_HOME}/server/bin
SOURCE_INFA_DEFAULT_DOMAIN=<YOUR_DOMAIN_NAME>
SOURCE_INFA_DEFAULT_DOMAIN_USER=<INFORMATICA_USER_WITH_DEPLOY_PRIVS>
SOURCE_INFA_DEFAULT_DOMAIN_PASSWORD=<PASSWORD_ENCRYPTED_WITH_PMPASSWD>
SOURCE_MRS=<MODEL_REPOSITORY_NAME>
SOURCE_DIS=<DATA_INTEGRATION_SERVICE_NAME>
# Note: DIS is only needed by some modules, ie. runMapping

##
# general
export LOGDIR
export RESULTDIR
export CONFIGDIR
##
# informatica
export SOURCE_INFACMD_LOCATION
export SOURCE_INFA_DEFAULT_DOMAIN
export SOURCE_INFA_DEFAULT_DOMAIN_USER
export SOURCE_INFA_DEFAULT_DOMAIN_PASSWORD
export SOURCE_MRS
export SOURCE_DIS
