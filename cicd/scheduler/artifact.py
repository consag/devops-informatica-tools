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
from cicd.scheduler import schedulerConstants as constants
from cicd.scheduler import schedulerSettings as settings
import supporting.deploylist
from pathlib import Path
from cicd.scheduler.schedulerArtifactChecks import checkSchedulerEntryType
from supporting import filehandling
import supporting.generalSettings as generalSettings

logger = logging.getLogger(__name__)
entrynr = 0
level = 0


def processList(deployFile):
    latestError = err.OK
    result, deployItems = supporting.deploylist.getWorkitemList(deployFile)
    if result.rc == err.OK.rc:
        filehandling.copy_file(deployFile, generalSettings.artifactDir)
        filehandling.create_directory(settings.targetschedulertypedir)
        filehandling.create_directory(settings.targetschedulerdir)
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

    type, directory, file = deployEntry.split(':', 3)
    supporting.log(logger, logging.DEBUG, thisproc,
                   'Type is >' + type + '<, directory is >' + directory + '< and file is >' + file + '<')

    result = checkSchedulerEntryType(type)
    if result.rc != 0:
        supporting.log(logger, logging.DEBUG, thisproc,
                       "checkSchedulerEntryType returned >" + result.message + "<. Entry ignored.")
        return result

    filePath = Path(file)
    if filePath.is_file():
        supporting.log(logger, logging.DEBUG, thisproc, 'Found file >' + file + "<.")
        sourcedir = ""
    else:
        sourcedir = settings.sourceschedulerdir + "/"
        supporting.log(logger, logging.DEBUG, thisproc, 'schedule file >' + file + '< not found. Trying >'
                       + sourcedir + file + '<...')
        filePath = Path(sourcedir + file)
        if filePath.is_file():
            supporting.log(logger, logging.DEBUG, thisproc, 'Found schedule file >' + sourcedir + file + "<.")
        else:
            supporting.log(logger, err.SCHEDULERFILE_NF.level, thisproc,
                           "schedule file checked >" + sourcedir + file + "<. " + err.SCHEDULERFILE_NF.message)
            result = err.SCHEDULERFILE_NF
            return result

    if type == constants.JOBTYPE:
        supporting.log(logger, logging.DEBUG, thisproc, 'copying job type file >' + sourcedir + file
                       + "< to >" + settings.targetschedulertypedir + "<.")
        filehandling.copy_file(sourcedir + file, settings.targetschedulertypedir)
    else:
        if type == constants.JOBASCODE:
            supporting.log(logger, logging.DEBUG, thisproc, 'copying jobascode file >' + sourcedir + file
                           + "< to >" + settings.targetschedulerdir + "<.")
            filehandling.copy_file(sourcedir + file, settings.targetschedulerdir)
        else:
            supporting.log(logger, logging.WARN, thisproc, 'invalid type >' + type + '<. Entry ignored.')

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


def determineSourceDirectory(directory, type):
    thisproc = "determineSourceDirectory"

    # type_path = directory + "/" + type
    type_path = directory
    directoryPath = Path(type_path)
    if directoryPath.is_dir():
        supporting.log(logger, logging.DEBUG, thisproc, 'Found directory >' + type_path + "<.")
        directory = type_path
    else:
        sourceDir = determinebaseSourceDirectory(type) + "/"
        supporting.log(logger, logging.DEBUG, thisproc, 'directory >' + type_path + '< not found. Trying >'
                       + sourceDir + type_path + '<...')
        type_path = sourceDir + type_path
        directoryPath = Path(type_path)
        if directoryPath.is_dir():
            supporting.log(logger, logging.DEBUG, thisproc, 'Found directory >' + type_path + "<.")
        else:
            supporting.log(logger, err.SQLFILE_NF.level, thisproc,
                           "directory checked >" + type_path + "<. " + err.DIRECTORY_NF.message)
            result = err.DIRECTORY_NF
            return constants.NOT_SET, result

    return type_path, err.OK
