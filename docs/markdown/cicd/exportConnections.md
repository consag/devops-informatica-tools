Module cicd.exportConnections
=============================

Functions
---------

    
`main(argv)`
:   Exports the connection definitions from the Informatica Domain.
    Usage: exportConnections.py [-h] [-o OUTPUT_FILE] [-e EXPORT_CONTROL_FILE]
    If no output file is provided, the default is set as per infaConstants.DEFAULT_EXPORT_CONNECTIONSFILE
    For information about the export control file, check the Informatica documentation.

    
`parse_the_arguments(argv)`
:   Parses the provided arguments and exits on an error.
    Use the option -h on the command line to get an overview of the required and optional arguments.