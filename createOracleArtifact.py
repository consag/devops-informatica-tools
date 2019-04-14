##
# Create Oracle Database Artifact
# @Since: 22-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190322.0 - JBE - Initial

import logging, datetime, supporting
import supporting.errorcodes as err
import databaseArtifact.databaseArtifactChecks as dbchecks
import databaseArtifact.processDatabaseDeployList
import databaseArtifact.dbSettings as settings
import supporting.generalSettings as generalsettings

now = datetime.datetime.now()
result = err.OK


def main():
    thisproc = "MAIN"
    mainProc='CreateOracleArtifact'

    resultlogger = supporting.configurelogger(mainProc)
    logger = logging.getLogger(mainProc)

    supporting.log(logger, logging.DEBUG, thisproc, 'Started')
    supporting.log(logger, logging.DEBUG, thisproc, 'logDir is >' + generalsettings.logDir + "<.")

    # Check requirements for artifact generation
    settings.getdbenvvars()
    result = dbchecks.databaseartifactchecks()
    if result.rc != 0:
        supporting.log(logger, logging.ERROR, thisproc, 'Database Artifact Checks failed with >' + result.message +"<.")
        return result.rc

    result = databaseArtifact.processDatabaseDeployList.processList(settings.deploylist)

    supporting.log(logger, logging.DEBUG, thisproc, 'Completed with return code >' + str(result.rc)
                   + '< and result code >' + result.code + "<.")
    supporting.writeresult(resultlogger, result)
    return result.rc


main()
