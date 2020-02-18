"""IDQ Importer Exporter

This script defines Import and Export functions through which it can communicate with
a Informatica Model Repository.

It also provides some related functions, such as:
	- Create IDQ folder
	- Check in IDQ components

    Parts by Laurens Verhoeven
    Parts by Jac. Beekers
    @Version: 20190412.0  - JBE - Initial version to work with deploy lists
    @License: MIT
"""

#  MIT License
#
#  Copyright (c) 2019 Jac. Beekers
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#

import datetime
import supporting, logging

from cicd.informatica import buildCommand
from cicd.informatica import executeInfacmd
from cicd.informatica import infaConstants as constants

logger = logging.getLogger(__name__)


def import_infadeveloper(**KeyWordArguments):
    """Import IDQ Components"""

    KeyWordArguments["Tool"] = "Import"
    ImportCommand = buildCommand.build(**KeyWordArguments)

    result = executeInfacmd.execute(ImportCommand, constants.DEPLOYARTIFACT)

    return result


def export_infadeveloper(**KeyWordArguments):
    thisproc = "export_infadeveloper"

    KeyWordArguments["Tool"] = "Export"
    ExportCommand = buildCommand.build(**KeyWordArguments)

    supporting.log(logger, logging.INFO, thisproc, "ExportCommand is >" + ExportCommand + "<.")
    result = executeInfacmd.execute(ExportCommand, constants.CREATEARTIFACT)

    return result


def CreateFolder(**KeyWordArguments):
    """Create IDQ Folder"""

    KeyWordArguments["Tool"] = "CreateFolder"

    CreateFolder = buildCommand.build(**KeyWordArguments)

    output, error = executeInfacmd.execute(CreateFolder)

    return (output, error)


def ListCheckedOutObjects(**KeyWordArguments):
    thisproc = "ListCheckedOutObjects"
    """ List Components that are currently checked out """

    KeyWordArguments["Tool"] = "ListCheckOutObjects"
    ListCheckedOutCommand = buildCommand.build(**KeyWordArguments)
    output, error = executeInfacmd.execute(ListCheckedOutCommand)

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

    supporting.log(logger, logging.DEBUG, thisproc, output)

    return Objects


def CheckIn(**KeyWordArguments):
    """Check-in IDQ Components"""

    KeyWordArguments["Tool"] = "CheckIn"
    CheckInCommand = buildCommand.build(**KeyWordArguments)
    output, error = executeInfacmd.execute(CheckInCommand)

    return (output, error)


def CheckInMutiple(**KeyWordArguments):
    thisproc = "CheckInMultiple"
    """ Check in Multiple IDQ components """
    for key, value in KeyWordArguments.items():
        if key == "MultipleObjectPaths":
            ObjectPaths = KeyWordArguments["MultipleObjectPaths"]

    KeyWordArguments["Tool"] = "CheckIn"

    CheckInCommands = []
    for ObjectPathName in ObjectPaths:
        KeyWordArguments["ObjectPathName"] = ObjectPathName
        CheckInCommands.append(buildCommand.build(**KeyWordArguments))

    CheckInAllCommand = "\n".join(CheckInCommands)

    timebefore = datetime.datetime.now()
    output, error = executeInfacmd.execute(CheckInAllCommand)
    timeafter = datetime.datetime.now()
    duration = timeafter - timebefore

    supporting.log(logging.DEBUG, thisproc,
                   "Infacmd took " + str(duration) + " seconds to check-in " + str(len(ObjectPaths)) + " objects")

    # output, error = (CheckInAllCommand, 0)

    return (output, error)


def create_iar_file(**KeyWordArguments):
    thisproc = "create_iar_file"

    KeyWordArguments["Tool"] = "CreateIAR"
    create_command = buildCommand.build(**KeyWordArguments)

    supporting.log(logger, logging.INFO, thisproc, "Command is >" + create_command + "<.")
    result = executeInfacmd.execute(create_command, constants.CREATEARTIFACT)

    return result


def deploy_iar_file(**KeyWordArguments):
    thisproc = "deploy_iar_file"

    KeyWordArguments["Tool"] = "DeployIAR"
    deploy_command = buildCommand.build(**KeyWordArguments)

    supporting.log(logger, logging.INFO, thisproc, "Command is >" + deploy_command + "<.")
    result = executeInfacmd.execute(deploy_command, constants.DEPLOYARTIFACT)

    return result

