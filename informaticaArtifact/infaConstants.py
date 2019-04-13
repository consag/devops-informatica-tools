##
# Informatica constants
# @Since: 10-APR-2019
# @Author: Jac. Beekers
# @License: MIT
# @Version: 20190410.0 - Initial

## Environment variables
# Informatica artifacts and deploys
varDeveloperDeployList = 'DEVELOPER_DEPLOYLIST'
varSourceInfaHome = 'SOURCE_INFA_HOME'
varSourceInfacmdLocation = 'SOURCE_INFACMD_LOCATION'
varSourceDomain = 'SOURCE_INFA_DEFAULT_DOMAIN'
varSourceModelRepository = 'SOURCE_MRS'
varSourceUsername = 'SOURCE_INFA_DEFAULT_DOMAIN_USER'
varSourcePassword = 'SOURCE_INFA_DEFAULT_DOMAIN_PASSWORD'
varSourceSecurityDomain = 'SOURCE_INFA_DEFAULT_SECURITY_DOMAIN'
varSourceDomainInfa ='SOURCE_INFA_DOMAINS_FILE'
#
varTargetInfaHome = 'TARGET_INFA_HOME'
varTargetInfacmdLocation = 'TARGET_INFACMD_LOCATION'
varTargetDomain = 'TARGET_INFA_DEFAULT_DOMAIN'
varTargetModelRepository = 'TARGET_MRS'
varTargetUsername = 'TARGET_INFA_DEFAULT_DOMAIN_USER'
varTargetPassword = 'TARGET_INFA_DEFAULT_DOMAIN_PASSWORD'
varTargetSecurityDomain = 'TARGET_INFA_DEFAULT_SECURITY_DOMAIN'
varTargetDomainInfa ='TARGET_INFA_DOMAINS_FILE'
##
# Defaults
DEFAULT_DEVELOPER_DEPLOYLIST = 'developer_deploylist.txt'
DEFAULT_INFA_HOME = '/appl/informatica/current'
DEFAULT_DOMAIN = 'DOM_Demo'
DEFAULT_MODEL_REPOSITORY = 'MRS_Demo'
DEFAULT_USERNAME = 'notReally'
DEFAULT_PASSWORD = 'W3Akrdu+PECXwqC/W21nXQ=='
DEFAULT_SECURITYDOMAIN = 'Native'

##
# Generic stuff
NOT_PROVIDED = "NotProvided"

##
# PowerCenter
varPowerCenterDeployList = 'POWERCENTER_DEPLOOYLIST'
DEFAULT_POWERCENTER_DEPLOYLIST = 'powercenter_deploylist.txt'

##
# Informatica Connections
varConnectionPassword = 'INFA_DEFAULT_CONNECTION_PASSWORD'

##
# Lists
AvailableArguments = {
    "Domain": "-dn",
    "User": "-un",
    "Password": "-pd",
    "Service": "-sn",
    "SecurityDomain": "-sdn",
    "Repository": "-rs",
    "TargetFolder": "-tf",
    "ConflictResolution": "-cr",
    "FilePath": "-fp",
    "Path": "-p",
    "SourceProject": "-sp",
    "TargetProject": "-tp",
    "Project": "-pn",
    "SkipCRC": "-sc",
    "ControlFilePath": "-cp",
    "OverwriteExportFile": "-ow",
    "ByObjectPathName": "-bopn",
    "ByUser": "-bu",
    "ObjectPathName": "-opn"
}

AvailableTools = {
    "Import": ("oie", "ImportObjects"),
    "Export": ("oie", "ExportObjects"),
    "CreateFolder": ("mrs", "CreateFolder"),
    "ListCheckOutObjects": ("mrs", "listCheckedOutObjects"),
    "CheckIn": ("mrs", "checkInObject"),
}
