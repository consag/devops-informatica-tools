##
# Process deploy list for database artifacts
# @Since: 23-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190324.0 - JBE - Initial

import supporting.errorcodes as err
import supporting, logging
import supporting.filehandling as filehandling
import re
import databaseArtifact.dbSettings as settings
import supporting.deploylist

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
    supporting.log(logger, logging.DEBUG, thisproc, "Started to work on deploy entry >" + deployEntry + "<.")

    schema, sqlfile = deployEntry.split(':', 2)
    supporting.log(logger, logging.DEBUG, thisproc, 'Schema is >' + schema + '< and sqlfile is >' + sqlfile + '<')

    result = generate_orderedsql(schema, sqlfile)

    supporting.log(logger, logging.DEBUG, thisproc,
                   "Completed with rc >" + str(result.rc) + "< and code >" + result.code + "<.")
    return result


def generate_orderedsql(schema, input_sqlfile):
    thisproc = "generate_orderedsql"
    global entrynr
    result = err.OK

    the_source_sqldir  = settings.sourcesqldir + "/" + schema + "/"
    the_source_sqlfile = input_sqlfile
    entrynr = entrynr + 1
    orderedsqlfilename = settings.targetsqldir + "/" + "%02d" % entrynr + "_ordered.sql"

    filehandling.removefile(orderedsqlfilename)
    processlines(the_source_sqldir, the_source_sqlfile, orderedsqlfilename)

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

def processlines(the_source_sqldir, the_source_sqlfile, orderedsqlfilename):
    result = err.OK
    global level
    level +=1
    thisproc="processlines-" + "%03d" % level
    supporting.log(logger, logging.DEBUG, thisproc, "level is >" + "%03d" % level +"<.")

    try:
        with open(the_source_sqldir + the_source_sqlfile) as thesql:
            for line in thesql:
                if (ignoreline(line)):
                    continue
                if (calltosubsql(line)):
                    supporting.log(logger, logging.DEBUG, thisproc, "Found '@@', a call to another script.")
                    write2file(orderedsqlfilename, "-- Start expansion -- " + line)
                    subsql = line[2:-1].split(' ', 1)[0]
                    completepathsql = the_source_sqldir + subsql
                    supporting.log(logger, logging.DEBUG, thisproc, "Sub file name determined as >" + subsql +"<. Complete file path >"
                                   + completepathsql +"<.")
                    #thesubsqlfile = the_source_sqldir + subsql
                    processlines(the_source_sqldir, subsql, orderedsqlfilename)
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
