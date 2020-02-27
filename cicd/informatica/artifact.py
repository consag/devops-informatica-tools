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
from supporting.artifactHandling import get_workspace
import cicd.informatica.infaConstants as infaConstants
import cicd.informatica.infaSettings as infaSettings
from cicd import informatica
from supporting.filehandling import copy_files
import os

logger = logging.getLogger(__name__)
entrynr = 0


def processList(what, deployFile):
    this_function = "processList"
    latest_result = err.OK
    overall_result = err.OK

    supporting.log(logger, logging.DEBUG, this_function, "deployfile is >" + deployFile + "<.")
    result, deploy_items = supporting.deploylist.getWorkitemList(deployFile)
    if result.rc == 0:
        if what == infaConstants.DEPLOY_APP:
            for deployEntry in deploy_items:
                latest_result = process_deploy_app_entry(what, deployEntry)
                if latest_result.rc != err.OK.rc:
                    overall_result = latest_result
            return overall_result
        elif what == infaConstants.CREATE_APP:
            for deployEntry in deploy_items:
                latest_result = process_create_app_entry(what, deployEntry)
                if latest_result.rc != err.OK.rc:
                    overall_result = latest_result
            return overall_result
        elif what == infaConstants.CREATEARTIFACT:
            supporting.log(logger, logging.DEBUG, this_function,
                           "Copying files in >" + os.path.dirname(deployFile) + "< to artifact.")
            copy_files(os.path.dirname(deployFile), generalSettings.artifactDir)
        # the following also executes if what = deploy artifact
        for deployEntry in deploy_items:
            latest_result = processEntry(what, deployEntry)
            if latest_result.rc != err.OK.rc:
                overall_result = latest_result
        return overall_result
    else:
        supporting.log(logger, logging.ERROR, this_function, "Could not get deploylist")
        return errorcodes.FILE_NF


def process_create_app_entry(what, deployEntry):
    global entrynr
    thisproc = "process_create_app_entry"
    result = err.OK

    entrynr += 1
    supporting.log(logger, logging.DEBUG, thisproc,
                   "Started to work on deploy entry# >" + str(entrynr) + "< being >" + deployEntry + "<.")
    parts = deployEntry.split(':')
    if not len(parts) == 2:
        supporting.log(logger, logging.DEBUG, thisproc,
                       "Insufficient entries found. Expected 2, got >" + str(len(parts)) + "<.")
        return err.IGNORE

    app_path = parts[0]
    supporting.log(logger, logging.DEBUG, thisproc, 'app_path is >' + app_path + '<')
    result = create_iar_file(app_path)

    return result


def process_deploy_app_entry(what, deployEntry):
    global entrynr
    thisproc = "process_deploy_app_entry"
    result = err.OK

    entrynr += 1
    supporting.log(logger, logging.DEBUG, thisproc,
                   "Started to work on deploy entry# >" + str(entrynr) + "< being >" + deployEntry + "<.")
    parts = deployEntry.split(':')
    if not len(parts) == 2:
        supporting.log(logger, logging.DEBUG, thisproc,
                       "Insufficient entries found. Expected 2, got >" + str(len(parts)) + "<.")
        return err.IGNORE

    app_path = parts[0]
    logical_dis_name = parts[1]

    # find the actual DIS name
    actual_dis_name = infaSettings.get_dis_name(logical_dis_name)

    supporting.log(logger, logging.DEBUG, thisproc, 'app_path is >' + app_path + '<, logical_dis_name is >'
                   + logical_dis_name +'<, actual_dis_name is >' + actual_dis_name + '<.')
    result = deploy_iar_file(app_path, actual_dis_name)

    return result


def processEntry(what, deployEntry):
    global entrynr
    thisproc = "processEntry"
    result = err.OK

    entrynr += 1
    supporting.log(logger, logging.DEBUG, thisproc,
                   "Started to work on deploy entry# >" + str(entrynr) + "< being >" + deployEntry + "<.")

    parts = deployEntry.split(':')
    if not len(parts) == 2 and not len(parts) >= 4:
        supporting.log(logger, logging.WARNING, thisproc,
                       "Insufficient entries found. Expected 2 or 4, got >" + str(len(parts)) + "<. Entry IGNORED")
        return err.IGNORE

    type = parts[0]
    object = parts[1]
    if len(parts) >= 4:
        exportcontrol_file = parts[2]
        basename_ecf = exportcontrol_file.split('.')[0]
        export_control = completePath(generalSettings.configDir + "/" + exportcontrol_file, generalSettings.sourceDir)
        supporting.log(logger, logging.DEBUG, thisproc, 'exportcontrolfile is >' + exportcontrol_file
                       + "< and its complete path is >" + export_control + "<. basename is >" + basename_ecf + "<.")

        importcontrol_file = parts[3]
        basename_icf = importcontrol_file.split('.')[0]
        import_control = completePath(infaSettings.targetInformaticaDir + "/" + importcontrol_file,
                                      generalSettings.sourceDir)
        supporting.log(logger, logging.DEBUG, thisproc, 'importcontrolfile is >' + importcontrol_file + "<."
                       + "< and its complete path is >" + import_control + "<. basename is >" + basename_icf + "<.")
    else:
        export_control = ""
        import_control = ""

    supporting.log(logger, logging.DEBUG, thisproc, 'Type is >' + type + '< and object is >' + object + '<')
    if what == infaConstants.CREATEARTIFACT:
        result = create_artifact(type, object, export_control, basename_ecf)
    elif what == infaConstants.DEPLOYARTIFACT:
        result = deploy_artifact(type, object, import_control, basename_ecf)
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
            Project=object,
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

    #    workspace = get_workspace()
    workspace = infaSettings.targetInformaticaDir

    if type == 'PROJECT':
        result = informatica.import_infadeveloper(
            Domain=infaSettings.targetDomain,
            Repository=infaSettings.targetModelRepository,
            Project=object,
            ImportFilePath=workspace + "/" + object + "." + import_filename + ".xml",
            ExportRefData=infaSettings.targetExportRefData
        )
    elif type == 'CONTROLFILE':
        result = informatica.import_infadeveloper(
            Domain=infaSettings.targetDomain,
            Repository=infaSettings.targetModelRepository,
            ImportFilePath=workspace + "/" + object + "_" + str(entrynr) + "." + import_filename + ".xml",
            ControlFilePath=import_control
        )
    else:
        result = errorcodes.NOT_IMPLEMENTED

    return result


def create_iar_file(app_path):
    result = informatica.create_iar_file(
        Domain=infaSettings.sourceDomain,
        Repository=infaSettings.sourceModelRepository,
        ApplicationPath=app_path,
        FilePath=generalSettings.artifactDir + "/",
    )

    return result


def deploy_iar_file(app_path, dis_name):
    result = informatica.deploy_iar_file(
        Domain=infaSettings.targetDomain,
        Repository=infaSettings.targetModelRepository,
        Application=app_path,
        ServiceName=dis_name,
        FilePath=generalSettings.artifactDir + "/",
    )

    return result