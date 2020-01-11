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
# fitnesseSettings
# @Since: 23-OCT-2019
# @Author: Jac. Beekers
# @Version: 20191023.0 - JBE - Initial
##

import cicd.fitnesse.fitnesseConstants as constants
import supporting, os, logging
import supporting.generalSettings as generalsettings
from supporting.generalSettings import completePath

logger = logging.getLogger(__name__)

sourcefitnessedir = constants.DEFAULT_SOURCE_FITNESSEDIR
targetfitnessedir = constants.DEFAULT_TARGET_FITNESSEDIR

def getfitnesseenvvars():
    thisproc="getfitnesseenvvars"
    global fitnessedeploylist, sourcefitnessedir, targetfitnessedir
    supporting.log(logger, logging.DEBUG, thisproc, 'started')
    fitnessedeploylist = completePath(os.environ.get(constants.varFitNesseDeployList, constants.DEFAULT_FITNESSE_DEPLOYLIST), generalsettings.sourceDir)
    sourcefitnessedir = completePath(os.environ.get(constants.varSourceFitNesseDir, constants.DEFAULT_SOURCE_FITNESSEDIR), generalsettings.sourceDir)
    targetfitnessedir = completePath(os.environ.get(constants.varTargetFitNesseDir, constants.DEFAULT_TARGET_FITNESSEDIR), generalsettings.sourceDir)


def outfitnesseenvvars():
    thisproc = "outfitnesseenvvars"
    supporting.log(logger, logging.INFO,  thisproc, 'fitnessedeploylist is >' + fitnessedeploylist + "<.")
    supporting.log(logger, logging.INFO,  thisproc, 'sourcefitnessedir is >' + sourcefitnessedir +"<.")
    supporting.log(logger, logging.INFO,  thisproc, 'targetfitnessedir is >' + targetfitnessedir +"<.")


