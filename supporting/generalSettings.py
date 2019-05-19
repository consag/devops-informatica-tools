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
# generalSettings
# @Since: 22-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190410.0 - JBE - Initial

import os, logging
import supporting
import supporting.generalConstants as constants

logger = logging.getLogger(__name__)

"""defaults"""
logDir = constants.DEFAULT_LOGDIR
resultDir = constants.DEFAULT_RESULTDIR
artifactDir = constants.DEFAULT_ARTIFACTDIR
configDir = constants.DEFAULT_CONFIGDIR
sourceDir = constants.DEFAULT_SOURCEDIR

def getenvvars():
    thisproc = "getenvvars"
    global logDir, resultDir, artifactDir, configDir, sourceDir, releaseID

    supporting.log(logger, logging.DEBUG, thisproc, 'started')

    logDir = os.environ.get(constants.varLogDir, constants.DEFAULT_LOGDIR)
    supporting.log(logger, logging.DEBUG, thisproc, 'logDir set to >' + logDir + "<.")

    resultDir = os.environ.get(constants.varResultDir, constants.DEFAULT_RESULTDIR)
    supporting.log(logger, logging.DEBUG, thisproc, 'resultDir set to >' + resultDir + "<.")

    artifactDir = os.environ.get(constants.varArtifactDir, constants.DEFAULT_ARTIFACTDIR)
    supporting.log(logger, logging.DEBUG, thisproc, 'artifactDir set to >' + artifactDir + "<.")

    configDir = os.environ.get(constants.varConfigDir, constants.DEFAULT_CONFIGDIR)
    supporting.log(logger, logging.DEBUG, thisproc, 'configDir set to >' + configDir + "<.")

    sourceDir = os.environ.get(constants.varSourceDir, constants.DEFAULT_SOURCEDIR)
    supporting.log(logger, logging.DEBUG, thisproc, 'sourceDir set to >' + sourceDir + "<.")

    releaseID = os.environ.get(constants.varReleaseId, constants.DEFAULT_RELEASEID)
    supporting.log(logger, logging.DEBUG, thisproc, 'releaseID set to >' + releaseID + "<.")

    supporting.log(logger, logging.DEBUG, thisproc, 'completed')


getenvvars()


def completePath(foundPath, prefixPath):
    if foundPath.startswith("/"):
        return foundPath
    else:
        return prefixPath +"/" + foundPath