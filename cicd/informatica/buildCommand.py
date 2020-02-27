#  MIT License
#
#  Copyright (c) 2019 ABN AMRO Bank N.V.
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
from supporting import generalConstants
from supporting import generalSettings
from cicd.informatica import infaConstants
from cicd.informatica import infaSettings
from supporting import log
import logging

logger = logging.getLogger(__name__)
entrynr = 0


def build(**KeyWordArguments):
    """Build an IDQ command, return it as string
    Process the input aruguments to compose the IDQ command
    This is done by first creating a list of strings, that are then joined to form the actual
    command
    The syntax used is as follows:
    $InfaPath + $InfaProgram + $InfaCommand + $InfaArguments
    """

    procName = "build"
    # Create the list that will hold the parts of the command, in order
    InfaArguments = []

    # Process each input argument.
    # The Tool arguments are processed separately, because those have to go first
    # For the other arguments, the order does not matter, so they can be processed together
    for key, value in KeyWordArguments.items():
        log(logger, logging.DEBUG, procName, "key =>" + key + "<.")
        if isinstance(value, str):
            if key.lower().__contains__("password"):
                log(logger, logging.DEBUG, procName, "value =>" + "***" + "<.")
            else:
                log(logger, logging.DEBUG, procName, "value =>" + value + "<.")
        # If the argument is "Tool" , assign the value to the variable Tool, and lookup the Program and
        # Command in AvailableTools, assign those to InfaProgram, InfaCommand
        if key == "Tool":
            Tool = KeyWordArguments["Tool"]
            (InfaProgram, InfaCommand) = infaConstants.AvailableTools[value]
        elif key == "Project":
            projectName = value
            InfaArguments.append(infaConstants.AvailableArguments[key] + " " + '"' + value + '"')
        elif key == "ExportRefData":
            if value == generalConstants.YES:
                InfaArguments.append(
                    "-oo " + '"' + "rtm:disName=" + infaSettings.sourceDIS + ",codePage=UTF-8,refDataFile=" +
                    generalSettings.artifactDir + "/" + projectName + ".zip" + '"')
        # If the argument is anything else, look it up in AvailableArguments and add the found
        # value to InfaArguments
        elif key in infaConstants.AvailableArguments:
            InfaArguments.append(infaConstants.AvailableArguments[key] + " " + '"' + value + '"')
        elif key == "AsIsOptions":
            new_value=value.lstrip('"').rstrip('"')
            log(logger, logging.DEBUG, procName, "stripped value =>" + new_value + "<.")
            InfaArguments.append(" " + new_value + " ")
        elif key == "OutputFile":
            InfaArguments.append(" >" + value + " ")
        elif key != "OnError":
            InfaArguments.append("-" + key + " " + '"' + value + '"')

    # Put all parts of the command in the same list, in correct order, and join them into one
    # string
    IDQCommandParts = [infaSettings.sourceInfacmd, InfaProgram, InfaCommand] + InfaArguments
    IDQCommand = " ".join(IDQCommandParts)

    return (IDQCommand)
