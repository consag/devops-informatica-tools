##
# Database Artifact Checks
# @Since: 22-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190322.0 - JBE - Initial

import supporting.errorcodes as err
import supporting, logging
import databaseArtifact.dbConstants as env
import databaseArtifact.dbSettings as settings
from pathlib import Path

logger = logging.getLogger(__name__)


def databaseartifactchecks():
    thisproc = "databaseartifactchecks"
    supporting.log(logger, logging.DEBUG, thisproc, 'started')
    result = err.OK

    if not settings.dbdeploylist:
        supporting.log(logger, err.NO_DEPLOYLIST.level, thisproc, err.NO_DEPLOYLIST.message)
        result = err.NO_DEPLOYLIST
    else:
        deploylistFile = Path(settings.dbdeploylist)
        if not deploylistFile.is_file():
            supporting.log(logger, err.DEPLOYLIST_NF.level, thisproc, "dbdeploylist is >" + settings.dbdeploylist +"<. " + err.DEPLOYLIST_NF.message)
            result = err.DEPLOYLIST_NF

    supporting.log(logger, logging.DEBUG, thisproc, 'completed with >' + str(result.rc) + "<.")
    return result
