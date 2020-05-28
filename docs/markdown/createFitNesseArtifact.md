Module createFitNesseArtifact
=============================
.. versionchanged:: 20200528.0
    * documentation only

Functions
---------

    
`main(argv)`
:   Creates a FitNesse artifact, consisting on collected test directories and files
    It uses a deploy list that contains subdirectories.
    Module uses environment variables that steer the artifact creation.
    
    Args:
        None

    
`parse_the_arguments(argv)`
:   Parses the provided arguments and exits on an error.
    Use the option -h on the command line to get an overview of the required and optional arguments.
    
    Args:
        argv: List containing command line arguments
    
    Returns:
        A list with validated command line arguments