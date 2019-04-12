##
# Create Oracle Database Artifact
# @Since: 22-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190322.0 - JBE - Initial

import logging, datetime, supporting
import supporting.errorcodes as err
import supporting.databaseArtifactChecks as dbchecks
import supporting.environmentChecks as envchecks
import supporting.dbConstants as constants
import databaseArtifact.processDatabaseDeployList
import supporting.dbSettings as settings
import supporting.generalSettings as generalsettings

now = datetime.datetime.now()
result = err.OK


def main():
    thisproc = "MAIN"
    mainProc='CreateOracleArtifact'

    supporting.configurelogger(mainProc)
    logger = logging.getLogger(mainProc)

    supporting.log(logger, logging.DEBUG, thisproc, 'Started')

    # Check environment, log etc
    result = envchecks.envArtifactChecks()
    if (result.rc != 0):
        supporting.exitscript(result)

    supporting.log(logger, logging.DEBUG, thisproc, 'logDir is >' + generalsettings.logDir + "<.")

    # Check requirements for artifact generation
    result = dbchecks.dbArtifactChecks()
    if (result.rc != 0):
        supporting.exitscript(result)

    result = databaseArtifact.processDatabaseDeployList.processList(settings.deploylist)

    supporting.log(logger, logging.DEBUG, thisproc, 'Completed with return code >' + str(result.rc)
                   + '< and result code >' + result.code + "<.")
    supporting.writeresult(result)
    return result.rc


main()
