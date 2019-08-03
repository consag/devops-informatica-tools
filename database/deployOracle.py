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
import supporting
import logging
import database.utilities.Oracle as util
from os import listdir
import sys
from supporting import generalSettings

logger = logging.getLogger(__name__)

class DeployOracle:

    def __init__(self):
        thisproc="init"
        self.logger = logging.getLogger(__name__)
        self.sqldir ="/tmp"
        self.target_owner =""
        self.db_properties_file =""

    def deployArtifact(self):
        thisproc="deployArtifact"
        log(self.logger, logging.INFO, thisproc, "deployArtifact started.")
        for sqlfile in listdir(self.sqldir):
            if sqlfile[-4:] != ".sql":
                log(self.logger, logging.INFO, thisproc, "Ignored non-sql file >" + sqlfile + "<.")
                continue
            log(self.logger, logging.INFO, thisproc, "Processing sql file >" + sqlfile + "<.")
            oracle_util = util.OracleUtilities('user','password','connection','REPORT','outputfile')
            oracle_util.run_sqlplus(sqlfile)

        log(self.logger, logging.INFO, thisproc, "deployArtifact completed.")

def main(argv):
    thisproc = "MAIN"
    mainProc='deployOracle'

    resultlogger = supporting.configurelogger(mainProc)
    logger = logging.getLogger(mainProc)

    generalSettings.getenvvars()

    supporting.log(logger, logging.DEBUG, thisproc, 'Started')
    supporting.log(logger, logging.DEBUG, thisproc, 'logDir is >' + generalSettings.logDir + "<.")

    depl = DeployOracle()
    depl.deployArtifact()

main(sys.argv[1:])
