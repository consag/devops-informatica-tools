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
# scheduler Artifact Checks
# @Since: 25-OCT-2019
# @Author: Jac. Beekers
# @Version: 20191025.0 - JBE - Initial

import supporting.errorcodes as err
import supporting, logging
from pathlib import Path
from cicd.scheduler import schedulerConstants as constants
from cicd.scheduler import schedulerSettings as settings

logger = logging.getLogger(__name__)


def schedulerartifactchecks():
    thisproc = "schedulerartifactchecks"
    supporting.log(logger, logging.DEBUG, thisproc, 'started')
    result = err.OK

    if not settings.schedulerdeploylist:
        supporting.log(logger, err.IGNORE.level, thisproc, err.NO_DEPLOYLIST.message)
        supporting.log(logger, err.IGNORE.level, thisproc, "Assuming scheduler is NOT part of the solution.")
        result = err.IGNORE
    else:
        deploylistFile = Path(settings.schedulerdeploylist)
        if not deploylistFile.is_file():
            supporting.log(logger, err.IGNORE.level, thisproc,
                           "schedulerdeploylist is >" + settings.schedulerdeploylist + "<. "
                           + err.DEPLOYLIST_NF.message + " - Schedule artifact IGNORED.")
            result = err.IGNORE

    supporting.log(logger, logging.DEBUG, thisproc, 'completed with >' + str(result.rc) + "<.")
    return result


def checkSchedulerEntryType(type):
    if type == constants.PLUGINS or type == constants.JOBTYPE:
        return err.OK
    if type == constants.DAGS or type == constants.JOBASCODE:
        return err.OK

    return err.INVALID_SCHEDULER_ENTRY_TYPE
