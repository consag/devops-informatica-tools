Module cicd.informatica.buildCommand
====================================

Functions
---------

    
`build(**KeyWordArguments)`
:   Build an IDQ command, return it as string
    Process the input aruguments to compose the IDQ command
    This is done by first creating a list of strings, that are then joined to form the actual
    command
    The syntax used is as follows:
    $InfaPath + $InfaProgram + $InfaCommand + $InfaArguments