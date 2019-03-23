##
# Check for generic environment settings
# @Since: 22-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190322.0 - JBE - Initial

import os, supporting.errorcodes as err
import supporting, logging
import supporting.environmentvars as env

def envArtifactChecks():
    thisProc="envArtifactChecks"
    supporting.log(logging.DEBUG, thisProc, 'started')

    supporting.log(logging.DEBUG, thisProc, 'Checking envvar >' + env.varLogDir +"<.")
    logDir = os.environ.get(env.varLogDir, None)
    if not logDir:
        retCode = err.LOGDIR_NOTSET.code
        retMsg = err.LOGDIR_NOTSET.message
        retResolution = err.LOGDIR_NOTSET.resolution + " " + env.varLogDir
        retArea = err.LOGDIR_NOTSET.area
        retLevel = err.LOGDIR_NOTSET.level
        supporting.log(retLevel, thisProc, retArea + " " + retCode + " " + retMsg + ": " + retResolution)
        supporting.log(logging.DEBUG, thisProc, 'completed with >' + err.LOGDIR_NOTSET.code +"<.")
        return err.LOGDIR_NOTSET

    supporting.log(logging.DEBUG, thisProc, 'setting LogDir to >' + logDir +"<.")
    supporting.LogDir=logDir
    supporting.log(logging.DEBUG, thisProc, 'LogDir is now >' + supporting.LogDir +"<.")

    supporting.log(logging.DEBUG, thisProc, 'completed with >' + str(err.OK.rc) +"<.")
    return err.OK