Module cicd.createOracleArtifact
================================

Functions
---------

    
`main(argv)`
:   Creates an Oracle artifact, consisting on collected sql files
    It uses a deploy list that contains schema and init.sql. Check the OracleArtifact docs and examples for more info.
    Module uses environment variables that steer the artifact creation.

    
`parse_the_arguments(argv)`
:   Parses the provided arguments and exits on an error.
    Use the option -h on the command line to get an overview of the required and optional arguments.