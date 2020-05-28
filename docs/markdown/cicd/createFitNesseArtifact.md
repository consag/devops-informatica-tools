Module cicd.createFitNesseArtifact
==================================
@Name: Create FitNesse Artifact
@Since: 23-OCT-2019
@Author: Jac. Beekers
@Version: 20200528.0

Functions
---------

    
`main(argv)`
:   Creates a FitNesse artifact, consisting on collected test directories and files
    It uses a deploy list that contains subdirectories.
    Module uses environment variables that steer the artifact creation.

    
`parse_the_arguments(argv)`
:   Parses the provided arguments and exits on an error.
    Use the option -h on the command line to get an overview of the required and optional arguments.