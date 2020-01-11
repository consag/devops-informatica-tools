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

#  MIT License
#
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#
#

import logging, datetime, supporting
from supporting import errorcodes
from cicd.informatica import infaSettings
from cicd.informatica import infaConstants
from supporting import generalSettings
from cicd.informatica import manageConnection
import sys, argparse

now = datetime.datetime.now()
result = errorcodes.OK


def parse_the_arguments(argv):
    """Parses the provided arguments and exits on an error.
    Use the option -h on the command line to get an overview of the required and optional arguments.
     """
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--outputfile", required=False, action="store", dest="output_file",
                        help="File to export the connection definitions to. Tip: Include the path. Default is >"
                             + infaConstants.DEFAULT_EXPORT_CONNECTIONSFILE + ".")
    parser.add_argument("-e", "--exportcontrolfile", required=False, action="store", dest="export_control_file",
                        help="The export control file allows filtering and more. Check the Informatica documentation on the structure and possibilities. "
                             + "Tip: Include a path.")
    args = parser.parse_args()

    if args.output_file is None:
        args.output_file = infaConstants.DEFAULT_EXPORT_CONNECTIONSFILE

    if args.export_control_file is None:
        args.export_control_file = ""

    return args


def main(argv):
    """Exports the connection definitions from the Informatica Domain.
    Usage: exportConnections.py [-h] [-o OUTPUT_FILE] [-e EXPORT_CONTROL_FILE]
    If no output file is provided, the default is set as per infaConstants.DEFAULT_EXPORT_CONNECTIONSFILE
    For information about the export control file, check the Informatica documentation.
    """
    thisproc = "MAIN"
    mainProc = 'exportConnections'

    resultlogger = supporting.configurelogger(mainProc)
    logger = logging.getLogger(mainProc)

    args = parse_the_arguments(argv)

    generalSettings.getenvvars()

    supporting.log(logger, logging.DEBUG, thisproc, 'Started')
    supporting.log(logger, logging.DEBUG, thisproc, 'logDir is >' + generalSettings.logDir + "<.")

    output_file = args.output_file
    export_control_file = args.export_control_file

    infaSettings.getinfaenvvars()
    infaSettings.outinfaenvvars()

    if export_control_file != "":
        connection = manageConnection.ManageConnection(Tool="ExportConnections",
                                                       Domain=infaSettings.sourceDomain,
                                                       ExportControlfile=export_control_file,
                                                       ExportFile=output_file,
                                                       RetainPassword='true',
                                                       Force='true',
                                                       OnError=errorcodes.INFACMD_EXPORT_CONN_FAILED
                                                       )
    else:
        connection = manageConnection.ManageConnection(Tool="ExportConnections",
                                                       Domain=infaSettings.sourceDomain,
                                                       ExportFile=output_file,
                                                       RetainPassword='true',
                                                       Force='true',
                                                       OnError=errorcodes.INFACMD_EXPORT_CONN_FAILED
                                                       )

    result = connection.manage()

    supporting.log(logger, logging.DEBUG, thisproc, 'Completed with return code >' + str(result.rc)
                   + '< and result code >' + result.code + "<.")
    supporting.exitscript(resultlogger, result)


if __name__ == '__main__':
    main(sys.argv[1:])
