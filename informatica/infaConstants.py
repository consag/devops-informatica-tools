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
# Informatica constants
# @Since: 10-APR-2019
# @Author: Jac. Beekers
# @License: MIT
# @Version: 20190410.0 - Initial
import supporting.generalConstants as generalConstants

## Environment variables
# Informatica artifacts and deploys
varDeveloperDeployList = 'DEVELOPER_DEPLOYLIST'
varOverwriteExportFile = 'OVERWRITE_EXPORT_FILE'

varSourceExportRefData = 'SOURCE_EXPORT_REFDATA'
varSourceInfaHome = 'SOURCE_INFA_HOME'
varSourceInfacmdLocation = 'SOURCE_INFACMD_LOCATION'
varSourceDomain = 'SOURCE_INFA_DEFAULT_DOMAIN'
varSourceModelRepository = 'SOURCE_MRS'
varSourceUsername = 'SOURCE_INFA_DEFAULT_DOMAIN_USER'
varSourcePassword = 'SOURCE_INFA_DEFAULT_DOMAIN_PASSWORD'
varSourceSecurityDomain = 'SOURCE_INFA_DEFAULT_SECURITY_DOMAIN'
varSourceDomainInfa = 'SOURCE_INFA_DOMAINS_FILE'
varSourceDIS = 'SOURCE_DIS'
varExportControlFile = 'EXPORT_CONTROLFLE'
#
varTargetImportRefData = 'TARGET_IMPORT_REFDATA'
varTargetInfaHome = 'TARGET_INFA_HOME'
varTargetInfacmdLocation = 'TARGET_INFACMD_LOCATION'
varTargetDomain = 'TARGET_INFA_DEFAULT_DOMAIN'
varTargetModelRepository = 'TARGET_MRS'
varTargetUsername = 'TARGET_INFA_DEFAULT_DOMAIN_USER'
varTargetPassword = 'TARGET_INFA_DEFAULT_DOMAIN_PASSWORD'
varTargetSecurityDomain = 'TARGET_INFA_DEFAULT_SECURITY_DOMAIN'
varTargetDomainInfa = 'TARGET_INFA_DOMAINS_FILE'
varTargetDIS = 'TARGET_DIS'
varImportControlFile = 'IMPORT_CONTROLFLE'

# Nexus
varGroupId = "InformaticaPlatform"

##
# Defaults
DEFAULT_DEVELOPER_DEPLOYLIST = 'developer_deploylist.txt'
DEFAULT_OVERWRITE_EXPORT_FILE = generalConstants.TRUE
DEFAULT_EXPORT_REFDATA = generalConstants.YES
DEFAULT_IMPORT_REFDATA = generalConstants.YES
DEFAULT_EXPORT_CONTROLFILE = 'ecf_default.xml'
DEFAULT_IMPORT_CONTROLFILE = 'icf_default.xml'
##
# Defaults for client or server infaSettings
DEFAULT_INFA_HOME = '/appl/informatica/current'
DEFAULT_DOMAIN = 'DOM_Demo'
DEFAULT_MODEL_REPOSITORY = 'MRS_Demo'
DEFAULT_USERNAME = 'notReally'
DEFAULT_PASSWORD = 'W3Akrdu+PECXwqC/W21nXQ=='
DEFAULT_SECURITYDOMAIN = 'Native'
DEFAULT_DATAINTEGRATION_SERVICE = 'DIS_Demo01'
##
# Generic stuff
NOT_PROVIDED = "NotProvided"

##
# PowerCenter
varPowerCenterDeployList = 'POWERCENTER_DEPLOOYLIST'
DEFAULT_POWERCENTER_DEPLOYLIST = 'powercenter_deploylist.txt'

##
#
CREATEARTIFACT = 'CreateArtifact'
DEPLOYARTIFACT = 'DeployArtifact'

##
# Informatica Connections
varConnectionPassword = 'INFA_DEFAULT_CONNECTION_PASSWORD'

##
# Lists
AvailableArguments = {
    "Domain": "-DomainName",
    "User": "-UserName",
    "Service": "-sn",
    "SecurityDomain": "-SecurityDomain",
    "Repository": "-RepositoryService",
    "TargetFolder": "-tf",
    "ConflictResolution": "-cr",
    "FilePath": "-ExportFilePath",
    "Path": "-p",
    "SourceProject": "-sp",
    "TargetProject": "-tp",
    "Project": "-ProjectName",
    "SkipCRC": "-sc",
    "ControlFilePath": "-ControlFilePath",
    "OverwriteExportFile": "-OverwriteExportFile",
    "ByObjectPathName": "-bopn",
    "ByUser": "-bu",
    "ObjectPathName": "-opn",
    "OtherOptions": "-OtherOptions"
}

AvailableTools = {
    "Import": ("oie", "ImportObjects"),
    "Export": ("oie", "ExportObjects"),
    "CreateProject": ("mrs", "CreateProject"),
    "DeleteProject": ("mrs", "DeleteProject"),
    "CreateFolder": ("mrs", "CreateFolder"),
    "DeleteFolder": ("mrs", "DeleteFolder"),
    "ListCheckOutObjects": ("mrs", "listCheckedOutObjects"),
    "CheckIn": ("mrs", "checkInObject"),
    "RunProfile": ("ps", "Execute"),
    "RunScorecard": ("ps", "Execute"),
    "RunMapping": ("ms", "runMapping")
}
