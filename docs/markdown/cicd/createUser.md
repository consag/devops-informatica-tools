Module cicd.createUser
======================

Functions
---------

    
`main(argv)`
:   Create a user.
    If a password is not provided, one will be generated
    usage: createUser.py [-h] -u USERNAME [-p PASSWORD] -f FULLNAME
                     [-d DESCRIPTION] [-e EMAIL] [-n PHONENUMBER]

    
`parse_the_arguments(argv)`
:   Parses the provided arguments and exits on an error.
    Use the option -h on the command line to get an overview of the required and optional arguments.