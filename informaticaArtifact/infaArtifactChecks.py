##
# Database Artifact Checks
# @Since: 12-APR-2019
# @Author: Jac. Beekers
# @Version: 20190414.0 - JBE - Initial

import supporting.errorcodes as err
import supporting, logging
import informaticaArtifact.infaSettings as settings
from pathlib import Path

logger = logging.getLogger(__name__)


def infaartifactchecks():
    thisproc = "infaartifactchecks"
    supporting.log(logger, logging.DEBUG, thisproc, 'started')
    result = err.OK

    if not settings.infadeploylist:
        supporting.log(logger, err.NO_DEPLOYLIST.level, thisproc, err.NO_DEPLOYLIST.message)
        result = err.NO_DEPLOYLIST
    else:
        deploylistFile = Path(settings.infadeploylist)
        if not deploylistFile.is_file():
            supporting.log(logger, err.DEPLOYLIST_NF.level, thisproc, "dbdeploylist is >" + settings.infadeploylist +"<. " + err.DEPLOYLIST_NF.message)
            result = err.DEPLOYLIST_NF

    supporting.log(logger, logging.DEBUG, thisproc, 'completed with >' + str(result.rc) + "<.")
    return result
