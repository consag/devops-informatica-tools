##
# Check for generic environment settings
# @Since: 22-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190324.0 - JBE - Initial

import os, supporting.errorcodes as err
import supporting, logging
import supporting.constants as constants
import supporting.settings as settings

def envArtifactChecks():
    thisproc="envArtifactChecks"
    supporting.log(logging.DEBUG, thisproc, 'started')

    supporting.log(logging.DEBUG, thisproc, 'getting environment variables')
    settings.getenvvars()

    supporting.log(logging.DEBUG, thisproc, 'Checking envvar >' + constants.varLogDir +"<.")
    if not settings.logDir:
        retCode = err.LOGDIR_NOTSET.code
        retMsg = err.LOGDIR_NOTSET.message
        retResolution = err.LOGDIR_NOTSET.resolution + " " + constants.varLogDir
        retArea = err.LOGDIR_NOTSET.area
        retLevel = err.LOGDIR_NOTSET.level
        supporting.log(retLevel, thisproc, retArea + " " + retCode + " " + retMsg + ": " + retResolution)
        supporting.log(logging.DEBUG, thisproc, 'completed with >' + err.LOGDIR_NOTSET.code +"<.")
        return err.LOGDIR_NOTSET

    supporting.log(logging.DEBUG, thisproc, 'LogDir is now >' + settings.logDir +"<.")

    supporting.log(logging.DEBUG, thisproc, 'completed with >' + str(err.OK.rc) +"<.")
    return err.OK
