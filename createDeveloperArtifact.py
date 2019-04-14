##
# generalSettings
# @Since: 22-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190412.0 - JBE - Initial
##

import logging, datetime, supporting
import supporting.errorcodes as err
import informaticaArtifact.infaArtifactChecks as infachecks
import informaticaArtifact.developer.processDeveloperDeployList as processDeveloperDeployList
import informaticaArtifact.infaSettings as settings
import supporting.generalSettings as generalsettings
#import informaticaArtifact

now = datetime.datetime.now()
result = err.OK

def main():
    thisproc = "MAIN"
    mainProc='CreateDeveloperArtifact'

    resultlogger = supporting.configurelogger(mainProc)
    logger = logging.getLogger(mainProc)

    supporting.log(logger, logging.DEBUG, thisproc, 'Started')
    supporting.log(logger, logging.DEBUG, thisproc, 'logDir is >' + generalsettings.logDir + "<.")

    settings.getinfaenvvars()
    settings.outinfaenvvars()

    # Check requirements for artifact generation
    result = infachecks.infaartifactchecks()
    if result.rc != 0:
        supporting.log(logger, logging.ERROR, thisproc, 'INFA Checks failed with >' + result.message +"<.")
        supporting.exitscript(resultlogger, result)

    result = processDeveloperDeployList.processList(settings.infadeploylist)

    supporting.log(logger, logging.DEBUG, thisproc, 'Completed with return code >' + str(result.rc)
                   + '< and result code >' + result.code + "<.")
#    supporting.writeresult(resultlogger, result)
    supporting.exitscript(resultlogger, result)


main()
