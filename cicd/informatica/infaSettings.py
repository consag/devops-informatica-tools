#  MIT License
#
#  Copyright (c) 2019 Jac. Beekers
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#

##
# dbSettings
# @Since: 22-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190414.0 - JBE - Initial
##

from cicd.informatica import infaConstants as constants
import supporting, os, logging
import supporting.generalSettings as generalsettings
from supporting.generalSettings import completePath

logger = logging.getLogger(__name__)


##
# getInfaEnvironment
def getinfaenvvars():
    thisproc = "getinfaenvvars"
    global infadeploylist, infa_app_deploylist, overwriteExportFile, targetInformaticaDir
    global sourceExportRefData, sourceInfaHome, sourceInfacmdLocation, sourceInfacmdCommand, sourceInfacmd, \
        sourceDomainInfa, sourceDomain, sourceModelRepository, sourceUsername, sourcePassword, sourceSecurityDomain, \
        sourceDIS, exportControlFile
    global targetExportRefData, targetInfaHome, targetInfacmdLocation, targetInfacmdCommand, targetInfacmd, \
        targetDomainInfa, targetDomain, targetModelRepository, targetUsername, targetPassword, targetSecurityDomain, \
        targetDIS, importControlFile

    supporting.log(logger, logging.DEBUG, thisproc, 'started')
    infadeploylist = completePath(
        os.environ.get(constants.varDeveloperDeployList, constants.DEFAULT_DEVELOPER_DEPLOYLIST),
        generalsettings.sourceDir)
    infa_app_deploylist = completePath(
        os.environ.get(constants.var_developer_app_deploylist, constants.DEFAULT_DEVELOPER_APP_DEPLOYLIST),
        generalsettings.sourceDir)

    overwriteExportFile = os.environ.get(constants.varOverwriteExportFile, constants.DEFAULT_OVERWRITE_EXPORT_FILE)

    sourceExportRefData = os.environ.get(constants.varSourceExportRefData, constants.DEFAULT_EXPORT_REFDATA)
    sourceInfaHome = os.environ.get(constants.varSourceInfaHome, constants.DEFAULT_INFA_HOME)
    sourceInfacmdLocation = os.environ.get(constants.varSourceInfacmdLocation, sourceInfaHome + "/server/bin")
    sourceDomain = os.environ.get(constants.varSourceDomain, constants.DEFAULT_DOMAIN)
    sourceModelRepository = os.environ.get(constants.varSourceModelRepository, constants.DEFAULT_MODEL_REPOSITORY)
    sourceUsername = os.environ.get(constants.varSourceUsername, constants.DEFAULT_USERNAME)
    sourcePassword = os.environ.get(constants.varSourcePassword, constants.DEFAULT_PASSWORD)
    sourceSecurityDomain = os.environ.get(constants.varSourceSecurityDomain, constants.DEFAULT_SECURITYDOMAIN)
    sourceDomainInfa = os.environ.get(constants.varSourceDomainInfa, sourceInfaHome + "/domains.infa")
    if os.name == 'nt':
        sourceInfacmdCommand = 'infacmd.bat'
    else:
        sourceInfacmdCommand = 'infacmd.sh'
    sourceInfacmd = sourceInfacmdLocation + '/' + sourceInfacmdCommand
    sourceDIS = os.environ.get(constants.varSourceDIS, constants.DEFAULT_DATAINTEGRATION_SERVICE)
    exportControlFile = completePath(
        os.environ.get(constants.varExportControlFile, constants.DEFAULT_EXPORT_CONTROLFILE), generalsettings.sourceDir)

    targetExportRefData = os.environ.get(constants.varTargetImportRefData, constants.DEFAULT_IMPORT_REFDATA)
    targetInfaHome = os.environ.get(constants.varTargetInfaHome, constants.DEFAULT_INFA_HOME)
    targetInfacmdLocation = os.environ.get(constants.varTargetInfacmdLocation, targetInfaHome + "/server/bin")
    targetDomain = os.environ.get(constants.varTargetDomain, constants.DEFAULT_DOMAIN)
    targetModelRepository = os.environ.get(constants.varTargetModelRepository, constants.DEFAULT_MODEL_REPOSITORY)
    targetUsername = os.environ.get(constants.varTargetUsername, constants.DEFAULT_USERNAME)
    targetPassword = os.environ.get(constants.varTargetPassword, constants.DEFAULT_PASSWORD)
    targetSecurityDomain = os.environ.get(constants.varTargetSecurityDomain, constants.DEFAULT_SECURITYDOMAIN)
    targetDomainInfa = os.environ.get(constants.varTargetDomainInfa, sourceInfaHome + "/domains.infa")
    if os.name == 'nt':
        targetInfacmdCommand = 'infacmd.bat'
    else:
        targetInfacmdCommand = 'infacmd.sh'
    targetInfacmd = targetInfacmdLocation + '/' + targetInfacmdCommand
    targetDIS = os.environ.get(constants.varTargetDIS, constants.DEFAULT_DATAINTEGRATION_SERVICE)
    targetInformaticaDir = os.environ.get(constants.varTargetInformaticaDir, constants.DEFAULT_TARGET_INFORMATICADIR)

    importControlFile = completePath(
        os.environ.get(constants.varImportControlFile, constants.DEFAULT_IMPORT_CONTROLFILE), generalsettings.sourceDir)

    supporting.log(logger, logging.DEBUG, thisproc, 'completed')
    return


def outinfaenvvars():
    thisproc = "outinfaenvvars"
    supporting.log(logger, logging.DEBUG, thisproc, 'started')
    #no need to show source env vars when deploying
    # supporting.log(logger, logging.INFO, thisproc, constants.varSourceInfaHome + ' =>' + sourceInfaHome + "<.")
    ##
    # etc. etc.

    supporting.log(logger, logging.DEBUG, thisproc, 'completed')
    return


def getpwcenvvars():
    thisproc = "getpwcenvvars"
    global pwcdeploylist
    supporting.log(logger, logging.DEBUG, thisproc, 'started')

    pwcdeploylist = os.environ.get(constants.varDeveloperDeployList, constants.DEFAULT_DEVELOPER_DEPLOYLIST)

    supporting.log(logger, logging.DEBUG, thisproc, 'completed')
    return


def outpwcenvvars():
    thisproc = "outPwcEnvironment"
    supporting.log(logger, logging.DEBUG, thisproc, 'started')
    supporting.log(logger, logging.INFO, thisproc, constants.varPowerCenterDeployList + ' =>' + pwcdeploylist + "<.")
    ##
    # etc. etc.

    supporting.log(logger, logging.DEBUG, thisproc, 'completed')
    return


def getinfaenvvars_old():
    thisproc = "getinfaenvvars"
    global deploylist
    supporting.log(logger, logging.DEBUG, thisproc, 'started')

    deploylist = os.environ.get(constants.varDeveloperDeployList, constants.DEFAULT_DEVELOPER_DEPLOYLIST)

    supporting.log(logger, logging.DEBUG, thisproc, 'completed')
    return


def outinfaenvvars_old():
    thisproc = "outinfaenvvars"
    supporting.log(logger, logging.DEBUG, thisproc, 'started')
    supporting.log(logger, logging.DEBUG, thisproc, deploylist)

    supporting.log(logger, logging.DEBUG, thisproc, 'completed')
    return


def get_dis_name(logical_dis_name):

    actual_dis_name = os.environ.get(logical_dis_name, constants.NOT_PROVIDED)
    return actual_dis_name
