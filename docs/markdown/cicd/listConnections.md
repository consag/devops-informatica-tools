Module cicd.listConnections
===========================

Functions
---------

    
`main(argv)`
:   List the connections as available in the Informatica domain.
    Usage: listConnections.py [-h] [-o OUTPUT_FILE]
    If no output file is provided, the default will be taken from infaConstants.DEFAULT_CONNECTIONSFILE

    
`parse_the_arguments(argv)`
:   Parses the provided arguments and exits on an error.
    Use the option -h on the command line to get an overview of the required and optional arguments.