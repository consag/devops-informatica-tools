Module cicd.informatica
=======================
IDQ Importer Exporter

This script defines Import and Export functions through which it can communicate with
a Informatica Model Repository.

It also provides some related functions, such as:
        - Create IDQ folder
        - Check in IDQ components

    Parts by Laurens Verhoeven
    Parts by Jac. Beekers
    @Version: 20190412.0  - JBE - Initial version to work with deploy lists
    @License: MIT

Sub-modules
-----------
* cicd.informatica.application
* cicd.informatica.artifact
* cicd.informatica.buildCommand
* cicd.informatica.executeInfacmd
* cicd.informatica.infaAppChecks
* cicd.informatica.infaArtifactChecks
* cicd.informatica.infaConstants
* cicd.informatica.infaSettings
* cicd.informatica.jobManagement
* cicd.informatica.manageConnection
* cicd.informatica.manageFolder
* cicd.informatica.manageSecurity
* cicd.informatica.manageWorkflow

Functions
---------

    
`CheckIn(**KeyWordArguments)`
:   Check-in IDQ Components

    
`CheckInMutiple(**KeyWordArguments)`
:   

    
`CreateFolder(**KeyWordArguments)`
:   Create IDQ Folder

    
`ListCheckedOutObjects(**KeyWordArguments)`
:   

    
`create_iar_file(**KeyWordArguments)`
:   

    
`deploy_iar_file(**KeyWordArguments)`
:   

    
`export_infadeveloper(**KeyWordArguments)`
:   

    
`import_infadeveloper(**KeyWordArguments)`
:   Import IDQ Components

    
`redeploy_iar_file(**KeyWordArguments)`
:   

    
`stop_app(**KeyWordArguments)`
: