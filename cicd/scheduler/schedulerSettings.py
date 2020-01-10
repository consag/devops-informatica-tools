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
# schedulerSettings
# @Since: 25-OCT-2019
# @Author: Jac. Beekers
# @Version: 20191025.0 - JBE - Initial
##

from cicd.scheduler import schedulerConstants as constants
import supporting, os, logging
import supporting.generalSettings as generalsettings
from supporting.generalSettings import completePath

logger = logging.getLogger(__name__)

sourceschedulerdir = constants.DEFAULT_SOURCE_SCHEDULERDIR
sourceschedulertypedir = constants.DEFAULT_SOURCE_SCHEDULER_TYPEDIR
targetschedulerdir = constants.DEFAULT_TARGET_SCHEDULERDIR
targetschedulertypedir = constants.DEFAULT_TARGET_SCHEDULER_TYPEDIR
schedulerdeploylist = constants.DEFAULT_SCHEDULER_DEPLOYLIST

def getschedulerenvvars():
    thisproc = "getschedulerenvvars"
    global schedulerdeploylist, sourceschedulerdir, targetschedulerdir, sourceschedulertypedir, targetschedulertypedir
    supporting.log(logger, logging.DEBUG, thisproc, 'started')

    schedulerdeploylist = completePath(
        os.environ.get(constants.varSchedulerDeployList, constants.DEFAULT_SCHEDULER_DEPLOYLIST),
        generalsettings.sourceDir)
    sourceschedulerdir = completePath(
        os.environ.get(constants.varSourceSchedulerDir, constants.DEFAULT_SOURCE_SCHEDULERDIR),
        generalsettings.sourceDir)
    sourceschedulertypedir = completePath(
        os.environ.get(constants.varSourceSchedulerTypeDir, constants.DEFAULT_SOURCE_SCHEDULER_TYPEDIR),
        generalsettings.sourceDir)
    targetschedulerdir = completePath(
        os.environ.get(constants.varTargetSchedulerDir, constants.DEFAULT_TARGET_SCHEDULERDIR),
        generalsettings.sourceDir)
    targetschedulertypedir = completePath(
        os.environ.get(constants.varTargetSchedulerTypeDir, constants.DEFAULT_TARGET_SCHEDULER_TYPEDIR),
        generalsettings.sourceDir)


def outschedulerenvvars():
    thisproc = "outschedulerenvvars"
    supporting.log(logger, logging.INFO, thisproc, 'schedulerdeploylist is >' + schedulerdeploylist + "<.")
    supporting.log(logger, logging.INFO, thisproc, 'sourceschedulerdir is >' + sourceschedulerdir + "<.")
    supporting.log(logger, logging.INFO, thisproc, 'sourceschedulertypedir is >' + sourceschedulertypedir + "<.")
    supporting.log(logger, logging.INFO, thisproc, 'targetschedulerdir is >' + targetschedulerdir + "<.")
    supporting.log(logger, logging.INFO, thisproc, 'targetschedulertypedir is >' + targetschedulertypedir + "<.")
