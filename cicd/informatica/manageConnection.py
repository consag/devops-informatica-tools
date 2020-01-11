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

from supporting import log
import logging
import supporting
from cicd.informatica import buildCommand
from cicd.informatica import executeInfacmd
from cicd.informatica import infaSettings
from supporting import errorcodes

class ManageConnection:

    def __init__(self, **keyword_arguments):
        self.logger = logging.getLogger(__name__)
        self.keyword_arguments = keyword_arguments
        self.connection_list =""

    def manage(self):
        RunCommand = buildCommand.build(**self.keyword_arguments)

        log(self.logger, logging.INFO, __name__, "RunCommand is >" + RunCommand + "<.")
        result = executeInfacmd.execute(RunCommand)

        if(result.rc != errorcodes.OK.rc):
            oldResult = result.message
            result = self.keyword_arguments["OnError"]
            result.message = oldResult

        return (result)

    def parseConnectionListOutput(self, outputFile):
        log(self.logger, logging.INFO, __name__, "Parsing outputfile >" + outputFile + "<.")

        with open(outputFile, 'r') as f:
            entireFile = [line.rstrip() for line in f]
        for line in entireFile:
            if 'ID:' in line:
                # found a connection
                connectionName, connectionId = line.split(' - ')
                ignoreThis, connectionId = connectionId.split(': ')
                connectionId = connectionId.rstrip(']')
                log(self.logger, logging.INFO, __name__, "Connection >" + connectionName + "< with id >"+ connectionId +"<.")
                connection_entry = connectionType.strip() + ":" + connectionId.strip() + ":" + connectionName.strip() + "\n"
                self.connection_list += connection_entry
            else:
                # it must be a connection type
                connectionType = line
                log(self.logger, logging.INFO, __name__, "Processing connection type >" + connectionType + "<.")

        return errorcodes.OK

    def writeConnectionList(self, outputFile):
        with open(outputFile, 'w') as f:
            f.write(self.connection_list)

        return errorcodes.OK

    def readConnectionList(self, inputFile):
        with open(inputFile, 'r') as f:
            self.connection_list = [line.rstrip() for line in f]
        return errorcodes.OK

    def getConnectionOptions(self, connection_name, output_file):
        this_proc = 'getConnectionOptions'
        connection = ManageConnection(Tool="ListConnectionOptions",
                                      Domain=infaSettings.sourceDomain,
                                      ConnectionName=connection_name,
                                      OnError=errorcodes.INFACMD_LIST_CONN_OPTIONS_FAILED,
                                      OutputFile=output_file
                                      )
        result = ManageConnection.manage(connection)
        if result.rc != errorcodes.OK.rc:
            with open(output_file, 'r') as f:
                for line in f:
                    result.message += line.rstrip()

        supporting.log(self.logger, logging.DEBUG, this_proc, 'Completed with return code >' + str(result.rc)
                       + '< and result code >' + result.code + "<.")

        return result

