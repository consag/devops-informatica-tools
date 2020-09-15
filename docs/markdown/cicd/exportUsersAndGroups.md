Module cicd.exportUsersAndGroups
================================

Functions
---------

    
`main(argv)`
:   Exports users and groups.
    usage: exportUsersAndGroups.py [-h] -o OUTPUT_FILE [-f {false,true}]
                               [-r {false,true}]
    where:
    -f or --force: Overwrite output file if it exists
    -r or --retainpassword: If set to "false" user passwords are not exported. If "true" they will be.

    
`parse_the_arguments(argv)`
:   Parses the provided arguments and exits on an error.
    Use the option -h on the command line to get an overview of the required and optional arguments.