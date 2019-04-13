##
# dbSettings
# @Since: 22-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190412.0 - JBE - Initial
##

import informaticaArtifact.infaConstants as constants
import supporting, os, logging
logger = logging.getLogger(__name__)

#infadeploylist = constants.DEFAULT_DEVELOPER_DEPLOYLIST

##
# getInfaEnvironment
def getinfaenvvars():
    thisproc="getinfaenvvars"
    global infadeploylist, overwriteExportFile
    global sourceExportRefData, sourceInfaHome, sourceInfacmdLocation, sourceInfacmdCommand, sourceInfacmd,\
        sourceDomainInfa, sourceDomain, sourceModelRepository, sourceUsername, sourcePassword, sourceSecurityDomain,\
        sourceDIS, exportControlFile
    global targetExportRefData, targetInfaHome, targetInfacmdLocation, targetInfacmdCommand, targetInfacmd,\
        targetDomainInfa, targetDomain, targetModelRepository, targetUsername, targetPassword, targetSecurityDomain,\
        targetDIS, importControlFile

    supporting.log(logger, logging.DEBUG, thisproc, 'started')
    infadeploylist = os.environ.get(constants.varDeveloperDeployList, constants.DEFAULT_DEVELOPER_DEPLOYLIST)
    overwriteExportFile = os.environ.get(constants.varOverwriteExportFile, constants.DEFAULT_OVERWRITE_EXPORT_FILE)

    sourceExportRefData = os.environ.get(constants.varSourceExportRefData, constants.DEFAULT_EXPORT_REFDATA)
    sourceInfaHome = os.environ.get(constants.varSourceInfaHome, constants.DEFAULT_INFA_HOME)
    sourceInfacmdLocation = os.environ.get(constants.varSourceInfacmdLocation, sourceInfaHome +"/server/bin")
    sourceDomain = os.environ.get(constants.varSourceDomain, constants.DEFAULT_DOMAIN)
    sourceModelRepository = os.environ.get(constants.varSourceModelRepository, constants.DEFAULT_MODEL_REPOSITORY)
    sourceUsername = os.environ.get(constants.varSourceUsername, constants.DEFAULT_USERNAME)
    sourcePassword = os.environ.get(constants.varSourcePassword, constants.DEFAULT_PASSWORD)
    sourceSecurityDomain = os.environ.get(constants.varSourceSecurityDomain, constants.DEFAULT_SECURITYDOMAIN)
    sourceDomainInfa = os.environ.get(constants.varSourceDomainInfa, sourceInfaHome + "/domains.infa")
    if os.name == 'nt':
        sourceInfacmdCommand ='infacmd.bat'
    else:
        sourceInfacmdCommand ='infacmd.sh'
    sourceInfacmd = sourceInfacmdLocation +'/' + sourceInfacmdCommand
    sourceDIS = os.environ.get(constants.varSourceDIS, constants.DEFAULT_DATAINTEGRATION_SERVICE)
    exportControlFile = os.environ.get(constants.varExportControlFile, constants.DEFAULT_EXPORT_CONTROLFILE)

    targetExportRefData = os.environ.get(constants.varTargetImportRefData, constants.DEFAULT_IMPORT_REFDATA)
    targetInfaHome = os.environ.get(constants.varTargetInfaHome, constants.DEFAULT_INFA_HOME)
    targetInfacmdLocation = os.environ.get(constants.varTargetInfacmdLocation, targetInfaHome +"/server/bin")
    targetDomain = os.environ.get(constants.varTargetDomain, constants.DEFAULT_DOMAIN)
    targetModelRepository = os.environ.get(constants.varTargetModelRepository, constants.DEFAULT_MODEL_REPOSITORY)
    targetUsername = os.environ.get(constants.varTargetUsername, constants.DEFAULT_USERNAME)
    targetPassword = os.environ.get(constants.varTargetPassword, constants.DEFAULT_PASSWORD)
    targetSecurityDomain = os.environ.get(constants.varTargetSecurityDomain, constants.DEFAULT_SECURITYDOMAIN)
    targetDomainInfa = os.environ.get(constants.varTargetDomainInfa, sourceInfaHome + "/domains.infa")
    if os.name == 'nt':
        targetInfacmdCommand ='infacmd.bat'
    else:
        targetInfacmdCommand ='infacmd.sh'
    targetInfacmd = targetInfacmdLocation +'/' + targetInfacmdCommand
    targetDIS = os.environ.get(constants.varTargetDIS, constants.DEFAULT_DATAINTEGRATION_SERVICE)
    importControlFile = os.environ.get(constants.varImportControlFile, constants.DEFAULT_IMPORT_CONTROLFILE)

    supporting.log(logger, logging.DEBUG, thisproc, 'completed')
    return

def outinfaenvvars():
    thisproc="outinfaenvvars"
    supporting.log(logger, logging.DEBUG, thisproc, 'started')
    supporting.log(logger, logging.INFO, thisproc, constants.varDeveloperDeployList + ' =>' + infadeploylist +"<.")
    supporting.log(logger, logging.INFO, thisproc, constants.varSourceInfaHome + ' =>' + sourceInfaHome +"<.")
    ##
    # etc. etc.

    supporting.log(logger, logging.DEBUG, thisproc, 'completed')
    return

def getpwcenvvars():
    thisproc="getpwcenvvars"
    global pwcdeploylist
    supporting.log(logger, logging.DEBUG, thisproc, 'started')

    pwcdeploylist = os.environ.get(constants.varDeveloperDeployList, constants.DEFAULT_DEVELOPER_DEPLOYLIST)

    supporting.log(logger, logging.DEBUG, thisproc, 'completed')
    return

def outpwcenvvars():
    thisproc="outPwcEnvironment"
    supporting.log(logger, logging.DEBUG, thisproc, 'started')
    supporting.log(logger, logging.INFO, thisproc, constants.varPowerCenterDeployList + ' =>' + pwcdeploylist +"<.")
    ##
    # etc. etc.

    supporting.log(logger, logging.DEBUG, thisproc, 'completed')
    return



def getinfaenvvars_old():
    thisproc="getinfaenvvars"
    global deploylist
    supporting.log(logger, logging.DEBUG, thisproc, 'started')

    deploylist = os.environ.get(constants.varDeveloperDeployList, constants.DEFAULT_DEVELOPER_DEPLOYLIST)

    supporting.log(logger, logging.DEBUG, thisproc, 'completed')
    return


def outinfaenvvars_old():
    thisproc="outinfaenvvars"
    supporting.log(logger, logging.DEBUG, thisproc, 'started')
    supporting.log(logger, logging.DEBUG, thisproc, deploylist)

    supporting.log(logger, logging.DEBUG, thisproc, 'completed')
    return
