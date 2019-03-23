##
# Errorcodes
# @Since: 22-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190322.0 - JBE - Initial

import logging
import supporting.errorcode as err

# Returncode, ErrorCode, ErrorMessage, Resolution, Area, Severity

OK=err.Errorcode(0,'0','No errors encounterued.','No action needed.','Result',logging.INFO)
##
LOGDIR_NOTSET=err.Errorcode(1,'ENV-0001','LOGDIR not defined','Set the environment variable','Environment',logging.FATAL)
LOGDIR_NF=err.Errorcode(1,'ENV-0002','LOGDIR not found','Set the environment variable to an existing directory','Environment',logging.FATAL)
LOGDIR_NW=err.Errorcode(1,'ENV-0003','Cannot write to LOGDIR','Set the environment variable to a writeable directory','Environment',logging.FATAL)

# Database artifact errors. Return code will be 10
NO_DEPLOYLIST=err.Errorcode(10,'DBDEPLOY-0001','No deploylist defined','Set the environment variable','DatabaseArtifact',logging.FATAL)

