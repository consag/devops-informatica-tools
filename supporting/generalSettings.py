##
# generalSettings
# @Since: 22-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190410.0 - JBE - Initial

import os, logging
import supporting
import supporting.generalConstants as constants

logger = logging.getLogger(__name__)

#global logDir
logDir=constants.DEFAULT_LOGDIR

def getenvvars():
    thisproc="getenvvars"
    global logDir
    supporting.log(logger, logging.DEBUG, thisproc, 'started')

    logDir= os.environ.get(constants.varLogDir, constants.DEFAULT_LOGDIR)
    supporting.log(logger, logging.DEBUG, thisproc, 'logDir set to >' + logDir +"<.")

    supporting.log(logger, logging.DEBUG, thisproc, 'completed')



getenvvars()
