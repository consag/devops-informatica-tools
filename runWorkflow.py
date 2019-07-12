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

import logging, datetime, supporting
from supporting import errorcodes
from informatica import infaSettings
from supporting import generalSettings
from informatica import jobManagement
from informatica import infaConstants
import sys

now = datetime.datetime.now()
result = errorcodes.OK

def main(argv):
    thisproc = "MAIN"
    mainProc='runWorkflow'

    resultlogger = supporting.configurelogger(mainProc)
    logger = logging.getLogger(mainProc)

    generalSettings.getenvvars()

    supporting.log(logger, logging.DEBUG, thisproc, 'Started')
    supporting.log(logger, logging.DEBUG, thisproc, 'logDir is >' + generalSettings.logDir + "<.")

    if len(argv) < 3:
        supporting.log(logger, logging.ERROR, thisproc, 'You need to provide: applicationnanem workflowname true/false (for waiting or not).')
        result = errorcodes.INFACMD_NOWORKFLOW
        supporting.exitscript(resultlogger, result)

    application_name = argv[0]
    workflow_name = argv[1]
    wait = argv[2]
    as_is_options = argv[3] if len(argv) > 3 else ""

    infaSettings.getinfaenvvars()
    infaSettings.outinfaenvvars()

    """with AsIsOptions, you can speficy e.g. a parameter set
        Example:
        runMapping myApp myMapping Source 3 "-ParameterSet myParameterSet -OperatingSystemProfile myOSProfile"
        It is important to supply the AsIsOptions as one single string
    """
    workflow = jobManagement.JobExecution(Tool="RunWorkflow",  # this will translate to StartWorkflow for the infacmd
                                         Domain=infaSettings.sourceDomain,
                                         ServiceName=infaSettings.sourceDIS,
                                         Application=application_name,
                                         Workflow=workflow_name,
                                         Wait=wait,
                                         OnError=errorcodes.INFACMD_WORKFLOW_FAILED,
                                         AsIsOptions=as_is_options
                                         )
    result = jobManagement.JobExecution.manage(workflow)

    supporting.log(logger, logging.DEBUG, thisproc, 'Completed with return code >' + str(result.rc)
                   + '< and result code >' + result.code + "<.")
    supporting.exitscript(resultlogger, result)


main(sys.argv[1:])
