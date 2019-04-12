##
# informaticaArtifact - init
# @Since: 22-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190410.0 - JBE - Initial
##
import supporting, logging, os
import supporting.infaConstants as constants
logger = logging.getLogger(__name__)

def getInfaEnvironment():
    thisproc="getInfaEnvironment"
    global infadeploylist
    global sourceInfaHome, sourceInfacmdLocation, sourceInfacmdCommand, sourceInfacmd\
        , sourceDomainInfa, sourceDomain, sourceModelRepository, sourceUsername, sourcePassword, sourceSecurityDomain
    global targetInfaHome, targetInfacmdLocation, targetInfacmdCommand, targetInfacmd\
        , targetDomainInfa, targetDomain, targetModelRepository, targetUsername, targetPassword, targetSecurityDomain

    supporting.log(logger, logging.DEBUG, thisproc, 'started')

    infadeploylist = os.environ.get(constants.varDeveloperDeployList, constants.DEFAULT_DEVELOPER_DEPLOYLIST)

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

    supporting.log(logger, logging.DEBUG, thisproc, 'completed')
    return

def outInfaEnvironment():
    thisproc="outInfaEnvironment"
    supporting.log(logging.DEBUG, thisproc, 'started')
    supporting.log(logging.INFO, thisproc, constants.varDeveloperDeployList + ' =>' + infadeploylist +"<.")
    supporting.log(logging.INFO, thisproc, constants.varSourceInfaHome + ' =>' + sourceInfaHome +"<.")
    ##
    # etc. etc.

    supporting.log(logging.DEBUG, thisproc, 'completed')
    return

def getPwcEnvironment():
    thisproc="getPwcEnvironment"
    global pwcdeploylist
    supporting.log(logging.DEBUG, thisproc, 'started')

    pwcdeploylist = os.environ.get(constants.varDeveloperDeployList, constants.DEFAULT_DEVELOPER_DEPLOYLIST)

    supporting.log(logging.DEBUG, thisproc, 'completed')
    return

def outPwcEnvironment():
    thisproc="outPwcEnvironment"
    supporting.log(logging.DEBUG, thisproc, 'started')
    supporting.log(logging.INFO, thisproc, constants.varPowerCenterDeployList + ' =>' + pwcdeploylist +"<.")
    ##
    # etc. etc.

    supporting.log(logging.DEBUG, thisproc, 'completed')
    return
