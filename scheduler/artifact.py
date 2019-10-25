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
import scheduler.schedulerConstants as constants
import scheduler.schedulerSettings as settings
import supporting.deploylist
from pathlib import Path

from scheduler.schedulerArtifactChecks import checkSchedulerEntryType
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

    type, directory, filter = deployEntry.split(':', 3)
    supporting.log(logger, logging.DEBUG, thisproc,
                   'Type is >' + type + '<, directory is >' + directory + '< and filter is >' + filter + '<')

    result = checkSchedulerEntryType(type)
    if result.rc != 0:
        return result

    zipfilename = determinebaseTargetDirectory(type) + "/" + directory.replace('/', '_') + ".zip"
    supporting.log(logger, logging.DEBUG, thisproc, 'zipfilename is >' + zipfilename + "<.")

    source_dir, result = determineSourceDirectory(directory)
    if result.rc != 0:
        return result

    result = generate_zip(source_dir, directory + "/" + filter, zipfilename)

    supporting.log(logger, logging.DEBUG, thisproc,
                   "Completed with rc >" + str(result.rc) + "< and code >" + result.code + "<.")

    return result


def determinebaseSourceDirectory(type):
    if type == constants.DAGS or type == constants.JOBASCODE:
        return settings.sourceschedulerdir
    if type == constants.PLUGINS or type == constants.JOBTYPE:
        return settings.sourceschedulertypedir

    return constants.NOT_SET


def determinebaseTargetDirectory(type):
    if type == constants.DAGS or type == constants.JOBASCODE:
        return settings.targetschedulerdir
    if type == constants.PLUGINS or type == constants.JOBTYPE:
        return settings.targetschedulertypedir

    return constants.NOT_SET


def determineSourceDirectory(directory):
    thisproc = "determineSourceDirectory"

    directoryPath = Path(directory)
    if directoryPath.is_dir():
        supporting.log(logger, logging.DEBUG, thisproc, 'Found directory >' + directory + "<.")
    else:
        sourceDir = determinebaseSourceDirectory(type) + "/"
        supporting.log(logger, logging.DEBUG, thisproc, 'directory >' + directory + '< not found. Trying >'
                       + sourceDir + directory + '<...')
        directory = sourceDir + directory
        directoryPath = Path(directory)
        if directoryPath.is_dir():
            supporting.log(logger, logging.DEBUG, thisproc, 'Found directory >' + directory + "<.")
        else:
            supporting.log(logger, err.SQLFILE_NF.level, thisproc,
                           "directory checked >" + directory + "<. " + err.DIRECTORY_NF.message)
            result = err.DIRECTORY_NF
            return constants.NOT_SET, result

    return directory, err.OK

