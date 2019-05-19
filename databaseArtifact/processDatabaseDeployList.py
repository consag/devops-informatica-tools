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

##
# Process deploy list for database artifacts
# @Since: 23-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190324.0 - JBE - Initial

import supporting.errorcodes as err
import supporting, logging
import supporting.filehandling as filehandling
import re, os
import databaseArtifact.dbSettings as settings
import supporting.generalSettings as generalSettings
import supporting.deploylist
from pathlib import Path

logger = logging.getLogger(__name__)
entrynr =0
level =0

def processList(deployFile):
    latestError = err.OK
    result, deployItems = supporting.deploylist.getWorkitemList(deployFile)
    if result.rc == 0:
        for deployEntry in supporting.deploylist.deployItems:
            result = processEntry(deployEntry)
            if result.rc != 0:
                latestError = result
    else:
        latestError = result
    return latestError

def processEntry(deployEntry):
    thisproc = "processEntry"
    result = err.OK
    supporting.log(logger, logging.DEBUG, thisproc, "Current directory is >" + os.getcwd() +"<.")
    supporting.log(logger, logging.DEBUG, thisproc, "Started to work on deploy entry >" + deployEntry + "<.")

    schema, sqlfile = deployEntry.split(':', 2)
    supporting.log(logger, logging.DEBUG, thisproc, 'Schema is >' + schema + '< and sqlfile is >' + sqlfile + '<')
    sqlfile = schema + "/" + sqlfile

    sqlfilePath = Path(sqlfile)
    if sqlfilePath.is_file():
        supporting.log(logger, logging.DEBUG, thisproc, 'Found sqlfile >' + sqlfile + "<.")
        sourcesqldir = ""
    else:
        sourcesqldir = settings.sourcesqldir + "/" + settings.databaseType + "/"
        supporting.log(logger, logging.DEBUG, thisproc, 'sqlfile >' + sqlfile + '< not found. Trying >'
                       + sourcesqldir + sqlfile + '<...')
#        sqlfile = sourcesqldir + sqlfile
        sqlfilePath = Path(sourcesqldir + sqlfile)
        if sqlfilePath.is_file():
            supporting.log(logger, logging.DEBUG, thisproc, 'Found sqlfile >' + sourcesqldir + sqlfile + "<.")
        else:
            supporting.log(logger, err.SQLFILE_NF.level, thisproc,
                       "sqlfile checked >" + sourcesqldir + sqlfile + "<. " + err.SQLFILE_NF.message)
            result = err.SQLFILE_NF
            return result

    result = generate_orderedsql(sourcesqldir, schema, sqlfile)

    supporting.log(logger, logging.DEBUG, thisproc,
                   "Completed with rc >" + str(result.rc) + "< and code >" + result.code + "<.")
    return result


def generate_orderedsql(sourcesqldir, schema, input_sqlfile):
    thisproc = "generate_orderedsql"
    global entrynr
    result = err.OK
    supporting.log(logger, logging.DEBUG, thisproc, "Started to work on sql file >" + input_sqlfile + "< in schema >" +schema +"<.")

    the_source_sqlfile = input_sqlfile
    entrynr = entrynr + 1
    ##
    # tricky: let's put the entrynr before the first _ we find (if any)
    prefixReleaseID = settings.sqlprefix +  generalSettings.releaseID
    if prefixReleaseID.find('_') >= 0:
        firstpart = prefixReleaseID[0:prefixReleaseID.find('_')] + ".%02d" % entrynr
        secondpart = prefixReleaseID[prefixReleaseID.find('_'):]
        prefixReleaseID = firstpart + secondpart

    orderedsqlfilename = settings.targetsqldir + "/" + prefixReleaseID \
                         + "_" + schema + ".sql"

    filehandling.removefile(orderedsqlfilename)
    result = processlines(sourcesqldir, schema, the_source_sqlfile, orderedsqlfilename)

    supporting.log(logger, logging.DEBUG, thisproc,
                   "Completed with rc >" + str(result.rc) + "< and code >" + result.code + "<.")

    return result

def ignoreline(line):
    if(re.match("^--", line) or re.match("^\n$",line)):
        return True
    return False


def calltosubsql(line):
    thisproc="calltosubsql"
    if(re.match("^@@", line)):
        return True
    return False

def processlines(the_source_sqldir, schema, the_source_sqlfile, orderedsqlfilename):
    result = err.OK
    global level
    level +=1
    thisproc="processlines-" + "%03d" % level
    supporting.log(logger, logging.DEBUG, thisproc, "level is >" + "%03d" % level +"<.")

    try:
        with open(the_source_sqldir + the_source_sqlfile) as thesql:
            for line in thesql:
                if ignoreline(line):
                    continue
                if calltosubsql(line):
                    supporting.log(logger, logging.DEBUG, thisproc, "Found '@@', a call to another script.")
                    write2file(orderedsqlfilename, "-- Start expansion -- " + line)
                    subsql = line[2:-1].split(' ', 1)[0]
                    completepathsql = the_source_sqldir + subsql
                    supporting.log(logger, logging.DEBUG, thisproc, "Sub file name determined as >" + subsql +"<. Complete file path >"
                                   + completepathsql +"<.")
                    processlines(the_source_sqldir, schema, schema +"/" + subsql, orderedsqlfilename)
                    write2file(orderedsqlfilename, "-- End expansion -- " + line)
                else:
                    write2file(orderedsqlfilename, line)

    except IOError:
        supporting.log(logger, logging.ERROR, thisproc, "Could not find file >" + the_source_sqlfile + "<.")
        write2file(orderedsqlfilename,"ERROR: Could not find file >" + the_source_sqlfile +"<.")
        result = err.FILE_NF

    return result

def write2file(filename, line):
    thisproc="write_sql"
    result = err.OK

    try:
        with open(filename, 'a') as the_result_file:
            if "\n" == line[-1]:
                the_result_file.write(line)
            else:
                the_result_file.write(line +"\n")
    except IOError:
        supporting.log(logger, logging.ERROR, thisproc, "Could not write to file >" + filename + "<.")
        result = err.FILE_NW

    return result
