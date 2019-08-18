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


from subprocess import Popen, PIPE
import logging
import supporting.errorcodes as err

logger = logging.getLogger(__name__)
from database import dbSettings
from supporting import log

logger = logging.getLogger(__name__)

class OracleUtilities:

    def __init__(self, db_user, db_password, db_connection, on_sql_error, output_file):
        self.database_connection = db_connection
        self.connect_string='connect ' + db_user + "/" + db_password + "@" + self.database_connection
        if on_sql_error == "ABORT":
           self.error_clause_sql="WHENEVER SQLERROR EXIT SQL.SQLCODE"
           self.error_clause_os="WHENEVER OSERROR EXIT 9"
        elif on_sql_error == "REPORT":
            self.error_clause_sql=""
            self.spool_clause_on="spool " + output_file
            self.spool_clause_off="spool off"
        else:
            self.error_clause_sql=""
            self.error_clause_os=""
            self.spool_clause_on=""
            self.spool_clause_off=""

    def run_sqlplus(self, sqlfile):
        thisproc = "run_sqlplus"
        result = err.OK

        try:
            log(logger, logging.INFO, thisproc, "Running script >" + sqlfile + "< on database >" + self.database_connection +"<.")
            p = Popen([dbSettings.sqlplus_command, "-s", "/NOLOG"], universal_newlines=True, stdin=PIPE, stdout=PIPE,
                                stderr=PIPE)
            stdoutput = p.communicate(input=self.error_clause_sql
                                            +"\n" + self.connect_string
                                            +"\n" + "@" + sqlfile
                                            +"\n" + "exit")[0]
            log(logger, logging.INFO, thisproc, "SQLPlus output: " + stdoutput)
            if p.returncode == 0:
                return err.OK
            else:
                err.SQLPLUS_ERROR.message = stdoutput
                return err.SQLPLUS_ERROR

        except FileNotFoundError as e:
            log(logger, logging.ERROR, thisproc, e.strerror +": " + dbSettings.sqlplus_command)
            return err.SQLFILE_NF

