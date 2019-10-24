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
# Process deploy list for Scheduler artifacts
# @Since: 25-OCT-2019
# @Author: Jac. Beekers
# @Version: 20191025.0 - JBE - Initial

import supporting.errorcodes as err
import supporting, logging
import os
import scheduler.schedulerSettings as settings
import supporting.deploylist
from pathlib import Path
from supporting.generatezip import generate_zip
from supporting.generatezip import addto_zip

logger = logging.getLogger(__name__)
entrynr = 0
level = 0


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
    supporting.log(logger, logging.DEBUG, thisproc, "Current directory is >" + os.getcwd() + "<.")
    supporting.log(logger, logging.DEBUG, thisproc, "Started to work on deploy entry >" + deployEntry + "<.")

    directory, suppress_zip = deployEntry.split(':', 2)
    supporting.log(logger, logging.DEBUG, thisproc,
                   'Directory is >' + directory + '< and suppress_zip is >' + suppress_zip + '<')
    zipfilename = settings.targetschedulerdir + "/" + directory.replace('/','_') + ".zip"
    supporting.log(logger, logging.DEBUG, thisproc, 'zipfilename is >' + zipfilename + "<.")

    directoryPath = Path(directory)
    if directoryPath.is_dir():
        supporting.log(logger, logging.DEBUG, thisproc, 'Found directory >' + directory + "<.")
        sourceschedulerdir = ""
    else:
        sourceschedulerdir = settings.sourceschedulerdir + "/"
        supporting.log(logger, logging.DEBUG, thisproc, 'directory >' + directory + '< not found. Trying >'
                       + sourceschedulerdir + directory + '<...')
        directory = sourceschedulerdir + directory
        directoryPath = Path(directory)
        if directoryPath.is_dir():
            supporting.log(logger, logging.DEBUG, thisproc, 'Found directory >' + directory + "<.")
        else:
            supporting.log(logger, err.SQLFILE_NF.level, thisproc,
                           "directory checked >" + directory + "<. " + err.DIRECTORY_NF.message)
            result = err.DIRECTORY_NF
            return result

    if suppress_zip == 'Y':
        supporting.log(logger, logging.DEBUG, thisproc, "zip files will be ignored.")
        result = generate_zip(sourceschedulerdir, directory, zipfilename, 'zip')
        result = addto_zip(sourceschedulerdir, directory + '.wiki', zipfilename, 'zip')
    else:
        supporting.log(logger, logging.DEBUG, thisproc, "zip files will be included.")
        result = generate_zip(sourceschedulerdir, directory, zipfilename)
        result = addto_zip(sourceschedulerdir, directory + '.wiki', zipfilename)

    supporting.log(logger, logging.DEBUG, thisproc,
                   "Completed with rc >" + str(result.rc) + "< and code >" + result.code + "<.")
    return result
