"""
    Process deploy list for database artifacts
    @Since: 23-MAR-2019
    @Author: Jac. Beekers
    @Version: 20190324.0 - JBE - Initial
"""

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

import supporting.errorcodes as err
import supporting, logging
import supporting.errorcodes as errorcodes
import supporting.deploylist
import supporting.generalSettings as generalSettings
from supporting.generalSettings import completePath
from supporting.artifactHandling import get_artifact
import cicd.informatica.infaConstants as infaConstants
import cicd.informatica.infaSettings as infaSettings
from cicd import informatica

logger = logging.getLogger(__name__)
entrynr = 0


def processList(what, deployFile):
    thisproc = "processList"
    latestResult = err.OK
    supporting.log(logger, logging.DEBUG, thisproc, "deployfile is >" + deployFile + "<.")
    result, deployItems = supporting.deploylist.getWorkitemList(deployFile)
    if result.rc == 0:
        for deployEntry in deployItems:
            latestResult = processEntry(what, deployEntry)
        return latestResult
    else:
        supporting.log(logger, logging.ERROR, thisproc, "Could not get deploylist")
        return errorcodes.FILE_NF


def processEntry(what, deployEntry):
    global entrynr
    thisproc = "processEntry"
    result = err.OK

    entrynr += 1
    supporting.log(logger, logging.DEBUG, thisproc,
                   "Started to work on deploy entry# >" + str(entrynr) + "< being >" + deployEntry + "<.")

    parts = deployEntry.split(':')
    if not len(parts) == 2 and not len(parts) == 4:
        supporting.log(logger, logging.DEBUG, thisproc,
                       "Insufficient entries found. Expected 2 or 4, got >" + str(len(parts)) + "<.")

    type = parts[0]
    object = parts[1]
    if len(parts) == 4:
        exportcontrol_file = parts[2]
        basename_ecf = exportcontrol_file.split('.')[0]
        exportcontrol = completePath(generalSettings.configDir + "/" + exportcontrol_file, generalSettings.sourceDir)
        supporting.log(logger, logging.DEBUG, thisproc, 'exportcontrolfile is >' + exportcontrol_file
                       + "< and its complete path is >" + exportcontrol + "<. basename is >" + basename_ecf + "<.")

        importcontrol_file = parts[3]
        basename_icf = importcontrol_file.split('.')[0]
        importcontrol = completePath(generalSettings.configDir + "/" + importcontrol_file, generalSettings.sourceDir)
        supporting.log(logger, logging.DEBUG, thisproc, 'importcontrolfile is >' + importcontrol_file + "<."
                       + "< and its complete path is >" + importcontrol + "<. basename is >" + basename_icf + "<.")
    else:
        exportcontrol = ""
        importcontrol = ""

    supporting.log(logger, logging.DEBUG, thisproc, 'Type is >' + type + '< and object is >' + object + '<')
    if what == infaConstants.CREATEARTIFACT:
        result = create_artifact(type, object, exportcontrol, basename_ecf)
    elif what == infaConstants.DEPLOYARTIFACT:
        result = deploy_artifact(type, object, importcontrol, basename_icf)
    else:
        result = errorcodes.COMMAND_FAILED

    supporting.log(logger, logging.DEBUG, thisproc,
                   "Completed with rc >" + str(result.rc) + "< and code >" + result.code + "<.")
    return result


def create_artifact(type, object, export_control="default.ecf", export_filename="export"):
    thisproc = 'create_artifact'
    supporting.log(logger, logging.DEBUG, thisproc,
                   "Creating artifact for object >" + object + "< of type >" + type + "<.")

    if type == 'PROJECT':
        result = informatica.export_infadeveloper(
            Domain=infaSettings.sourceDomain,
            Repository=infaSettings.sourceModelRepository,
            Project=object,
            FilePath=generalSettings.artifactDir + "/" + object + "." + export_filename + ".xml",
            OverwriteExportFile=infaSettings.overwriteExportFile,
            ExportRefData=infaSettings.sourceExportRefData
        )
    elif type == 'CONTROLFILE':
        result = informatica.export_infadeveloper(
            Domain=infaSettings.sourceDomain,
            Repository=infaSettings.sourceModelRepository,
            FilePath=generalSettings.artifactDir + "/" + object + "_" + str(entrynr) + "." + export_filename + ".xml",
            OverwriteExportFile=infaSettings.overwriteExportFile,
            ControlFilePath=export_control
        )
    else:
        result = errorcodes.NOT_IMPLEMENTED

    return result


def deploy_artifact(type, object, import_control, import_filename="export"):
    thisproc = 'deployArtifact'
    supporting.log(logger, logging.DEBUG, thisproc, 'started deploy for object >' + object + '<.')

    object_path = get_artifact(object)

    if type == 'PROJECT':
        result = informatica.import_infadeveloper(
            Domain=infaSettings.targetDomain,
            Repository=infaSettings.targetModelRepository,
            Project=object,
            FilePath=generalSettings.artifactDir + "/" + object + "." + import_filename + ".xml",
            ExportRefData=infaSettings.targetExportRefData
        )
    elif type == 'CONTROLFILE':
        result = informatica.import_infadeveloper(
            Domain=infaSettings.targetDomain,
            Repository=infaSettings.targetModelRepository,
            Project=object,
            # FilePath=generalSettings.artifactDir + "/" + object + "_" + str(entrynr) + "." + import_filename + ".xml",
            FilePath=object_path,
            ControlFilePath=import_control
        )
    else:
        result = errorcodes.NOT_IMPLEMENTED

    return result
