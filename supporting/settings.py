#!/usr/bin/env python2
import os, logging
import supporting.constants as constants
import supporting

#global logDir
logDir=constants.DEFAULT_LOGDIR
sourcesqldir = constants.DEFAULT_SOURCE_SQLDIR
targetsqldir = constants.DEFAULT_TARGET_SQLDIR

def getenvvars():
    thisproc="getenvvars"
    global logDir
    supporting.log(logging.DEBUG, thisproc, 'started')

    logDir= os.environ.get(constants.varLogDir, constants.DEFAULT_LOGDIR)
    supporting.log(logging.DEBUG, thisproc, 'logDir set to >' + logDir +"<.")

    supporting.log(logging.DEBUG, thisproc, 'completed')

def getdbenvvars():
    thisproc="getdbenvvars"
    global deploylist, sourcesqldir, targetsqldir
    supporting.log(logging.DEBUG, thisproc, 'started')

    deploylist = os.environ.get(constants.varOracleDeployList, constants.DEFAULT_ORACLE_DEPLOYLIST)
    sourcesqldir = os.environ.get(constants.varSourceSqlDir, constants.DEFAULT_SOURCE_SQLDIR)
    targetsqldir = os.environ.get(constants.varTargetSqlDir, constants.DEFAULT_TARGET_SQLDIR)

    supporting.log(logging.DEBUG, thisproc, 'completed')


getenvvars()
getdbenvvars()
