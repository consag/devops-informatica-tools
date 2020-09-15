Module cicd.deployOracle
========================
deployOracle

Functions
---------

    
`main(argv)`
:   Deploy the Oracle artifact to the target environment.
    Usage: deployOracle.py [-h] -s SCHEMA_NAME
    The module uses environment variables to steer the deployment,
    like target Oracle database, connections and such.
    For more information check the deployOracle docs.

    
`parse_the_arguments(argv)`
:   Parses the provided arguments and exits on an error.
    Use the option -h on the command line to get an overview of the required and optional arguments.

Classes
-------

`DeployOracle(schema)`
:   Deploys a previously built Oracle package

    ### Methods

    `deploy_artifact(self)`
    :   :return: result