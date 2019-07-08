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
import informatica.infaSettings as infaSettings
import supporting.generalSettings as generalSettings
from supporting.generalSettings import completePath
from supporting.artifactHandling import getInformaticaArtifact
from informatica import infaConstants
import informatica

logger = logging.getLogger(__name__)
entrynr =0

def processList(what, deployFile):
    thisproc = "processList"
    latestResult = err.OK
    supporting.log(logger, logging.DEBUG, thisproc, "deployfile is >" + deployFile +"<.")
    result, deployItems = supporting.deploylist.getWorkitemList(deployFile)
    if result.rc == 0:
        for deployEntry in deployItems:
            latestResult = processEntry(what, deployEntry)
        return latestResult
    else:
        supporting.log(logger, logging.ERROR, thisproc, "Could not get deploylist")
        return errorcodes.FILE_NF

def processEntry(what, deployEntry):
    thisproc = "processEntry"
    result = err.OK
    supporting.log(logger, logging.DEBUG, thisproc, "Started to work on deploy entry >" + deployEntry + "<.")

    parts = deployEntry.split(':')
    if not len(parts) == 2 and not len(parts) == 4:
        supporting.log(logger, logging.DEBUG, thisproc, "Insufficient entries found. Expected 2 or 4, got >" + str(len(parts)) +"<.")

    type = parts[0]
    object = parts[1]
    if len(parts) == 4:
        exportcontrol = completePath(generalSettings.configDir + "/" + parts[2], generalSettings.sourceDir)
        importcontrol = completePath(generalSettings.configDir + "/" + parts[3], generalSettings.sourceDir)

    supporting.log(logger, logging.DEBUG, thisproc, 'Type is >' + type + '< and object is >' + object + '<')
    if what == infaConstants.CREATEARTIFACT:
        result = create_artifact(type, object, exportcontrol)
    elif what == infaConstants.DEPLOYARTIFACT:
        result = deploy_artifact(type, object, importcontrol)
    else:
        result = errorcodes.COMMAND_FAILED

    supporting.log(logger, logging.DEBUG, thisproc,
                   "Completed with rc >" + str(result.rc) + "< and code >" + result.code + "<.")
    return result


def create_artifact(type, object, exportcontrol="default.ecf"):
    if type == 'PROJECT':
        result = informatica.export_infadeveloper(
            Domain=infaSettings.sourceDomain,
            Repository=infaSettings.sourceModelRepository,
            Project=object,
            FilePath=generalSettings.artifactDir + "/" + object +".xml",
            OverwriteExportFile=infaSettings.overwriteExportFile,
            ExportRefData=infaSettings.sourceExportRefData
        )
    elif type == 'CONTROLFILE':
        result = informatica.export_infadeveloper(
            Domain = infaSettings.sourceDomain,
            Repository = infaSettings.sourceModelRepository,
            Project=object,
            FilePath=generalSettings.artifactDir + "/" + object +".xml",
            OverwriteExportFile = infaSettings.overwriteExportFile,
            ControlFilePath = exportcontrol
        )
    else:
        result = errorcodes.NOT_IMPLEMENTED

    return result

def deploy_artifact(type, object, importcontrol):
    thisproc = 'deployArtifact'
    supporting.log(logger, logging.DEBUG, thisproc, 'started deploy for object >' + object +'<.')

    result = getInformaticaArtifact(object)
    if result.rc != 0:
        supporting. log(logger, logging.ERROR, thisproc, 'getInformaticaArtifact failed with >' + result.message +"<.")
        return result

    if type == 'PROJECT':
        result = informatica.import_infadeveloper(
            Domain=infaSettings.targetDomain,
            Repository=infaSettings.targetModelRepository,
            Project=object,
            FilePath=generalSettings.artifactDir + "/" + object +".xml",
            ExportRefData=infaSettings.targetExportRefData
        )
    elif type == 'CONTROLFILE':
        result = informatica.import_infadeveloper(
            Domain = infaSettings.targetDomain,
            Repository = infaSettings.targetModelRepository,
            Project=object,
            FilePath=generalSettings.artifactDir + "/" + object +".xml",
            ControlFilePath = importcontrol
        )
    else:
        result = errorcodes.NOT_IMPLEMENTED

    return result

