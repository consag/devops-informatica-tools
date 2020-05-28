Module cicd.listConnectionOptions
=================================

Functions
---------

    
`main(argv)`
:   List connection options for the provided connection definition.
    Usage: listConnectionOptions.py [-h] -c CONNECTION_NAME [-o OUTPUT_FILE]
    If no output file is provided, the default infaConstants.DEFAULT_CONNECTIONOPTIONSFILE will be used.

    
`parse_the_arguments(argv)`
:   Parses the provided arguments and exits on an error.
    Use the option -h on the command line to get an overview of the required and optional arguments.