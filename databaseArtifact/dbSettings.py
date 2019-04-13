##
# dbSettings
# @Since: 22-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190410.0 - JBE - Initial
##

import databaseArtifact.dbConstants as constants
import supporting, os, logging
logger = logging.getLogger(__name__)

sourcesqldir = constants.DEFAULT_SOURCE_SQLDIR
targetsqldir = constants.DEFAULT_TARGET_SQLDIR

def getdbenvvars():
    thisproc="getdbenvvars"
    global deploylist, sourcesqldir, targetsqldir
    supporting.log(logger, logging.DEBUG, thisproc, 'started')

    deploylist = os.environ.get(constants.varOracleDeployList, constants.DEFAULT_ORACLE_DEPLOYLIST)
    sourcesqldir = os.environ.get(constants.varSourceSqlDir, constants.DEFAULT_SOURCE_SQLDIR)
    targetsqldir = os.environ.get(constants.varTargetSqlDir, constants.DEFAULT_TARGET_SQLDIR)

    supporting.log(logger, logging.DEBUG, thisproc, 'completed')

