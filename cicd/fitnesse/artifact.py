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
# Process deploy list for FitNesse artifacts
# @Since: 23-OCT-2019
# @Author: Jac. Beekers
# @Version: 20191023.0 - JBE - Initial

import supporting.errorcodes as err
import supporting, logging
import os
import cicd.fitnesse.fitnesseSettings as settings
import supporting.deploylist
from pathlib import Path
from supporting.generatezip import generate_zip
from supporting.generatezip import addto_zip
from supporting.filehandling import copy_file
import supporting.generalSettings as generalSettings

logger = logging.getLogger(__name__)
entrynr = 0
level = 0
previous_schema = 'AUQW&^D*AD&FS'


def processList(deployFile):
    latestError = err.OK
    result, deployItems = supporting.deploylist.getWorkitemList(deployFile)
    if result.rc == err.OK.rc:
        copy_file(deployFile, generalSettings.artifactDir)
        for deployEntry in supporting.deploylist.deployItems:
            result = processEntry(deployEntry)
            if result.rc != 0:
                latestError = result
    else:
        # if no deploy list, then that is just fine.
        if result.rc == err.IGNORE.rc:
            latestError = err.OK
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
    zipfilename = settings.targetfitnessedir + "/" + directory.replace('/','_') + ".zip"
    supporting.log(logger, logging.DEBUG, thisproc, 'zipfilename is >' + zipfilename + "<.")

    directoryPath = Path(directory)
    if directoryPath.is_dir():
        supporting.log(logger, logging.DEBUG, thisproc, 'Found directory >' + directory + "<.")
        sourcefitnessedir = ""
    else:
        sourcefitnessedir = settings.sourcefitnessedir + "/"
        supporting.log(logger, logging.DEBUG, thisproc, 'directory >' + directory + '< not found. Trying >'
                       + sourcefitnessedir + directory + '<...')
        directory = sourcefitnessedir + directory
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
        result = generate_zip(sourcefitnessedir, directory, zipfilename, '*', 'zip')
        result = addto_zip(sourcefitnessedir, directory + '.wiki', zipfilename, '*', 'zip')
    else:
        supporting.log(logger, logging.DEBUG, thisproc, "zip files will be included.")
        result = generate_zip(sourcefitnessedir, directory, zipfilename)
        result = addto_zip(sourcefitnessedir, directory + '.wiki', zipfilename)

    supporting.log(logger, logging.DEBUG, thisproc,
                   "Completed with rc >" + str(result.rc) + "< and code >" + result.code + "<.")
    return result
