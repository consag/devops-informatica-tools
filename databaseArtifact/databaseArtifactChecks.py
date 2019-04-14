##
# Database Artifact Checks
# @Since: 22-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190322.0 - JBE - Initial

import supporting.errorcodes as err
import supporting, logging
import databaseArtifact.dbConstants as env
import databaseArtifact.dbSettings as settings

logger = logging.getLogger(__name__)


def databaseartifactchecks():
    thisproc = "databaseartifactchecks"
    supporting.log(logger, logging.DEBUG, thisproc, 'started')

    if not settings.deploylist:
        retCode = err.NO_DEPLOYLIST.code
        retMsg = err.NO_DEPLOYLIST.message
        retResolution = err.NO_DEPLOYLIST.resolution + " " + env.varOracleDeployList
        retArea = err.NO_DEPLOYLIST.area
        retLevel = err.NO_DEPLOYLIST.level
        supporting.log(logger, retLevel, thisproc, retArea + " " + retCode + " " + retMsg + ": " + retResolution)
        supporting.log(logger, logging.DEBUG, thisproc, 'completed with >' + retCode + "<.")
        return err.NO_DEPLOYLIST

    supporting.log(logger, logging.DEBUG, thisproc, 'completed with >' + str(err.OK.rc) + "<.")
    return err.OK