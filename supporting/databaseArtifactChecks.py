##
# Database Artifact Checks
# @Since: 22-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190322.0 - JBE - Initial

import os, supporting.errorcodes as err
import supporting, logging
import supporting.environmentvars as env

def dbArtifactChecks():
    thisProc="dbArtifactChecks"
    supporting.log(logging.DEBUG, thisProc, 'started')

    schemaname = os.environ.get(env.varOracleDeployList, None)
    if not schemaname:
        retCode = err.NO_DEPLOYLIST.code
        retMsg = err.NO_DEPLOYLIST.message
        retResolution = err.NO_DEPLOYLIST.resolution + " " + env.varOracleDeployList
        retArea = err.NO_DEPLOYLIST.area
        retLevel = err.NO_DEPLOYLIST.level
        supporting.log(retLevel, thisProc, retArea + " " + retCode + " " + retMsg + ": " + retResolution)
        supporting.log(logging.DEBUG, thisProc, 'completed with >' + retCode +"<.")
        return err.NO_DEPLOYLIST

    supporting.log(logging.DEBUG, thisProc, 'completed with >' + str(err.OK.rc) +"<.")
    return err.OK