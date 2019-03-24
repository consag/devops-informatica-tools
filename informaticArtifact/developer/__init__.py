"""IDQ Importer Exporter

This script defines Import and Export functions through which it can communicate with
a Informatica Data Quality Model Repository.

It also provides some related functions, such as:
	- Create IDQ folder
	- Check in IDQ components
"""

###############################################################################################
###############################################################################################
# To Do #######################################################################################
###############################################################################################

# - Get environment-dependent variables from bash profile

# Export IDQ component
# Check in imported components

# Global variable:
# - domain name
# - User name
# - Password
# - Security Domain (Native)
# - repository service
# -

# Input arguments:
# - Project name
# - export file path
# - component name(s)
# -


# # import os.path, time
# from os import listdir
# from os.path import isfile, join

# import lxml.etree as ET

import subprocess, datetime
from pprint import pprint, pformat
# from Logging import MyLogger
import supporting, logging


def ExecuteBash(bashCommands):
    """Execute a linux command"""
    thisproc = "ExecuteBash"

    supporting.log(logging.DEBUG, thisproc, "Executing commands: " + bashCommands)

    output, error = ("", 0)
    process = subprocess.Popen(bashCommands, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()

    return (output, error)


def ExecuteInfacmd(bashCommands):
    """Execute a linux command, after sourcing IDQ connection details """

    InitializationCommands = """. ~/.bash_profile 
    . ~/infa_env.sh

"""
    output, error = ExecuteBash(InitializationCommands + bashCommands)

    return (output, error)


def BuildCommand(**KeyWordArguments):
    """Build an IDQ command, return it as string"""

    # Create a lookup dictionary with the IDQ arguments recognized bu this function
    AvailableArguments = {
        "Domain": "-dn",
        "User": "-un",
        "Password": "-pd",
        "Service": "-sn",
        "SecurityDomain": "-sdn",
        "Repository": "-rs",
        "TargetFolder": "-tf",
        "ConflictResolution": "-cr",
        "FilePath": "-fp",
        "Path": "-p",
        "SourceProject": "-sp",
        "TargetProject": "-tp",
        "Project": "-pn",
        "SkipCRC": "-sc",
        "ControlFilePath": "-cp",
        "OverwriteExportFile": "-ow",
        "ByObjectPathName": "-bopn",
        "ByUser": "-bu",
        "ObjectPathName": "-opn",
        "MappingName": "-m",
        "ApplicationName": "-a",
    }

    # Create a lookup dictionary with the IDQ tools (program + command combination) recognized bu this function
    AvailableTools = {
        "Import": ("oie", "ImportObjects"),
        "Export": ("oie", "ExportObjects"),
        "CreateFolder": ("mrs", "CreateFolder"),
        "ListCheckOutObjects": ("mrs", "listCheckedOutObjects"),
        "CheckIn": ("mrs", "checkInObject"),
        "RunMapping": ("ms", "RunMapping"),
    }

    # Process the input aruguments to compose the IDQ command
    # This is doen by first creating a list of strings, that are then joined to form the actual
    # command
    # The syntax used is as follows:
    # $InfaPath + $InfaProgram + $InfaCommand + $InfaArguments

    # Create the list that will hold the parts of the command, in order
    InfaArguments = []

    # Process each input argument.
    # The InfaPath and Tool arguments are processed separetly, because those have to go first
    # For the other arguments, the order does not matter, so they can be processed togetehr
    for key, value in KeyWordArguments.items():
        # If the argument is "InfaPath" , assign the value to the variable InfaPath
        if key == "InfaPath":
            InfaPath = KeyWordArguments["InfaPath"]
        # If the argument is "Tool" , assign the value to the variable Tool, and lookup the Program and
        # Command in AvailableTools, assign those to InfaProgram, InfaCommand
        elif key == "Tool":
            Tool = KeyWordArguments["Tool"]
            (InfaProgram, InfaCommand) = AvailableTools[value]
        # If the argument is anything else, look it up in AvailableArguments and add the found
        # value to InfaArguments
        elif key in AvailableArguments:
            InfaArguments.append(AvailableArguments[key] + " " + '"' + value + '"')

    # Put all parts of the command in the same list, in correct order, and join them into one
    # string
    IDQCommandParts = [InfaPath, InfaProgram, InfaCommand] + InfaArguments
    IDQCommand = " ".join(IDQCommandParts)

    return (IDQCommand)


def Import(**KeyWordArguments):
    """Import IDQ Components"""

    KeyWordArguments["Tool"] = "Import"
    ImportCommand = BuildCommand(**KeyWordArguments)

    output, error = ExecuteInfacmd(ImportCommand)

    return (output, error)


def Export(**KeyWordArguments):
    """Export IDQ Components"""

    KeyWordArguments["Tool"] = "Export"
    ExportCommand = BuildCommand(**KeyWordArguments)
    output, error = ExecuteInfacmd(ExportCommand)

    return (output, error)


def CreateFolder(**KeyWordArguments):
    """Create IDQ Folder"""

    KeyWordArguments["Tool"] = "CreateFolder"

    CreateFolder = BuildCommand(**KeyWordArguments)

    output, error = ExecuteInfacmd(CreateFolder)

    return (output, error)


def ListCheckedOutObjects(**KeyWordArguments):
    """ List Components that are currently checked out """

    KeyWordArguments["Tool"] = "ListCheckOutObjects"
    ListCheckedOutCommand = BuildCommand(**KeyWordArguments)
    output, error = ExecuteInfacmd(ListCheckedOutCommand)

    # The output is in the form of one object per line, with properties spearated by a comma + space.
    # To filter out irrelevant lines, such as "Command succesful", we keep only line that start with "MRS_PATH="
    OutputLines = output.splitlines()
    OutputKeyValuePairLines = [Properties.split(", ") for Properties in OutputLines if
                               Properties.startswith("MRS_PATH=")]

    # ObjectsOLD = [[KVPair.split("=", 1) for KVPair in Line] for Line in OutputKeyValuePairLines]

    # Each object is a dictionary, with properties as keys
    # Since the date field has a comma in it, its not parsed properly. For this reason we need the len == 2 filter
    # If the date is required, the parsing of the output should be adjusted
    Objects = [dict(KVPair.split("=") for KVPair in Line if len(KVPair.split("=")) == 2) for Line in
               OutputKeyValuePairLines]

    print("")
    print(output)
    print("")

    return (Objects)


def CheckIn(**KeyWordArguments):
    """Check-in IDQ Components"""

    KeyWordArguments["Tool"] = "CheckIn"
    CheckInCommand = BuildCommand(**KeyWordArguments)
    output, error = ExecuteInfacmd(CheckInCommand)

    return (output, error)


def CheckInMutiple(**KeyWordArguments):
    """ Check in Multiple IDQ components """
    for key, value in KeyWordArguments.items():
        if key == "MultipleObjectPaths":
            ObjectPaths = KeyWordArguments["MultipleObjectPaths"]

    KeyWordArguments["Tool"] = "CheckIn"

    CheckInCommands = []
    for ObjectPathName in ObjectPaths:
        KeyWordArguments["ObjectPathName"] = ObjectPathName
        CheckInCommands.append(BuildCommand(**KeyWordArguments))

    CheckInAllCommand = "\n".join(CheckInCommands)

    timebefore = datetime.datetime.now()
    output, error = ExecuteInfacmd(CheckInAllCommand)
    timeafter = datetime.datetime.now()
    duration = timeafter - timebefore

    print("\nInfacmd took " + str(duration) + " seconds to check-in " + str(len(ObjectPaths)) + " objects\n")

    # output, error = (CheckInAllCommand, 0)

    return (output, error)


def RunMapping(**KeyWordArguments):
    """Run an IDQ mapping"""

    KeyWordArguments["Tool"] = "RunMapping"
    CheckInCommand = BuildCommand(**KeyWordArguments)
    output, error = ExecuteInfacmd(CheckInCommand)

    return (output, error)
