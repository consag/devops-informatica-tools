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

import logging, datetime, supporting
import supporting.errorcodes as err
from informaticaArtifact import infaSettings
from supporting import generalSettings
from informaticaArtifact.developer import dataProfiling
import sys

now = datetime.datetime.now()
result = err.OK

def main(argv):
    thisproc = "MAIN"
    mainProc='runScorecard'

    resultlogger = supporting.configurelogger(mainProc)
    logger = logging.getLogger(mainProc)

    generalSettings.getenvvars()

    supporting.log(logger, logging.DEBUG, thisproc, 'Started')
    supporting.log(logger, logging.DEBUG, thisproc, 'logDir is >' + generalSettings.logDir + "<.")

    if len(argv) == 0:
        supporting.log(logger, logging.ERROR, thisproc, 'No scorecard path specified.')
        result = err.INFACMD_NOSCORECARD
        supporting.exitscript(resultlogger, result)

    objectPath = argv[0]
    infaSettings.getinfaenvvars()
    infaSettings.outinfaenvvars()

    result = dataProfiling.runScorecard(
          Domain=infaSettings.sourceDomain,
            MrsServiceName=infaSettings.sourceModelRepository,
            DsServiceName=infaSettings.sourceDIS,
            ObjectPathAndName=objectPath,
            ObjectType="scorecard",
            Wait="true"
    )

    supporting.log(logger, logging.DEBUG, thisproc, 'Completed with return code >' + str(result.rc)
                   + '< and result code >' + result.code + "<.")
    supporting.exitscript(resultlogger, result)


main(sys.argv[1:])
