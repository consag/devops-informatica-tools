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

from supporting import log
import supporting
import logging
import database.utilities.Oracle as util
from os import listdir
import sys
from supporting import generalSettings
import database.dbSettings as dbSettings
import database.dbConstants as dbConstants

logger = logging.getLogger(__name__)

class DeployOracle:

    def __init__(self, schema):
        thisproc="init"
        self.logger = logging.getLogger(__name__)
        #self.sqldir ="/tmp"
        self.database_schema = schema
        dbSettings.getdbenvvars()
        self.database_tns_name, self.database_schema, self.database_user, self.database_user_password = dbSettings.getschemaenvvars(schema)
        self.sqldir = dbSettings.targetsqldir
        dbSettings.outdbenvvars()
        dbSettings.outschemaenvvars()
#        log(self.logger, logging.DEBUG, thisproc, 'database_tns_name is >' + self.database_tns_name +"<.")
#        log(self.logger, logging.DEBUG, thisproc, 'database_schema is >' + self.database_schema +"<.")
#        log(self.logger, logging.DEBUG, thisproc, 'database_user is >' + self.database_user + "<.")
#        if self.database_user_password is None or self.database_user_password == dbConstants.NOT_SET:
#            log(self.logger, logging.WARN, thisproc, 'database_user_password is empty.')
#        else:
#            log(self.logger, logging.DEBUG, thisproc, 'database_user_password has a value.')


    def deployArtifact(self):
        thisproc="deployArtifact"
        overall_result = 0
        log(self.logger, logging.INFO, thisproc, "deployArtifact started.")
        log(self.logger, logging.DEBUG, thisproc, "sqldir is >" + self.sqldir + "<")
        log(self.logger, logging.DEBUG, thisproc, "database_schema is >" + self.database_schema +"<.")
        schema_directory = self.sqldir + '/' + self.database_schema
        log(self.logger, logging.DEBUG, thisproc, "schema_directory is >" + schema_directory +"<.")
        for sqlfile in listdir(schema_directory):
            if sqlfile[-4:] != ".sql":
                log(self.logger, logging.INFO, thisproc, "Ignored non-sql file >" + sqlfile + "<.")
                continue
            log(self.logger, logging.INFO, thisproc, "Processing sql file >" + sqlfile + "<.")
            oracle_util = util.OracleUtilities(self.database_user,self.database_user_password,self.database_tns_name,'ABORT',self.database_schema +'_sqloutput.log')
            sqlplus_result = oracle_util.run_sqlplus(schema_directory +'/' + sqlfile)
            if sqlplus_result != 0:
                log(self.logger, logging.WARNING, thisproc, "sqlplus returned >" + sqlplus_result.code + "<.")
                overall_result = sqlplus_result

        log(self.logger, logging.INFO, thisproc, "deployArtifact completed with >" + overall_result.code +"<.")
        return overall_result


def main(argv):
    thisproc = "MAIN"
    mainProc='deployOracle'

    resultlogger = supporting.configurelogger(mainProc)
    logger = logging.getLogger(mainProc)

    generalSettings.getenvvars()

    supporting.log(logger, logging.DEBUG, thisproc, 'Started')
    supporting.log(logger, logging.DEBUG, thisproc, 'logDir is >' + generalSettings.logDir + "<.")

    if len(argv) == 0:
        supporting.log(logger, logging.ERROR, thisproc, "No schema specified. Supply one.")
        exit(1)
    else:
        schema = argv[0]
        supporting.log(logger, logging.INFO, thisproc, "Schema to deployed is >" +schema +"<.")
        depl = DeployOracle(schema)
        result = depl.deployArtifact()
        supporting.exitscript(resultlogger, result)

main(sys.argv[1:])
