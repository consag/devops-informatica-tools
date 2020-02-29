#  MIT License
#
#  Copyright (c) 2020 Jac. Beekers
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

from supporting import log
import logging
from cicd.informatica import buildCommand
from cicd.informatica import executeInfacmd
from supporting import errorcodes
from supporting.mask_password import mask_password
from cicd.informatica import infaConstants as constants
from cicd.informatica import infaSettings
import supporting
from supporting import filehandling
import sys


logger = logging.getLogger(__name__)

"""
    List Application objects
"""


def list(logical_dis_name):
    thisproc = 'list'
    """Runs Informatica command line to list applications deployed to a DIS
    """
    tmp_file_name = filehandling.generate_tmp_filename()
    supporting.log(logger, logging.DEBUG, thisproc, 'Started')

    actual_dis_name = infaSettings.get_dis_name(logical_dis_name)
    infaSettings.getinfaenvvars()

    run_command = buildCommand.build(
        Tool='ListApplications',
        Domain=infaSettings.sourceDomain,
        ServiceName=actual_dis_name,
        OutputFile=tmp_file_name
    )

    masked_run_command = mask_password(run_command)

    log(logger, logging.DEBUG, __name__, "RunCommand is >" + masked_run_command + "<.")
    result = executeInfacmd.execute(run_command)

    app_list = filehandling.convert_content_to_array(tmp_file_name)
    filehandling.removefile(tmp_file_name)

    supporting.log(logger, logging.DEBUG, thisproc, 'Completed')
    return result, app_list


def main(args):
    thisproc = 'main'
    supporting.log(logger, logging.DEBUG, thisproc, 'args is >' + args + '<.')
    print(args)
    result, app_list = list(args)
    supporting.log(logger, logging.DEBUG, thisproc, "result is >" + result.message + "<.")
    if app_list is None:
        supporting.log(logger, logging.ERROR, thisproc, 'app_list could not be determined.')
    else:
        for a in app_list:
            print(a)


if __name__ == '__main__':
    main(sys.argv[1])
