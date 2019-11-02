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

from supporting import log
import logging
from cicd.informatica import buildCommand
from cicd.informatica import executeInfacmd
from supporting import errorcodes
from supporting.mask_password import mask_password


class ManageSecurity:
    """Implements wrapper around security related commands, like create a user, a group and more."""

    def __init__(self, **keyword_arguments):
        self.logger = logging.getLogger(__name__)
        self.keyword_arguments = keyword_arguments

    def manage(self):
        """Runs Informatica command line to create, delete, update security related objects,
        like users and groups.
        """
        run_command = buildCommand.build(**self.keyword_arguments)

        masked_run_command = mask_password(run_command)

        log(self.logger, logging.DEBUG, __name__, "RunCommand is >" + masked_run_command + "<.")
        result = executeInfacmd.execute(run_command)

        if (result.rc != errorcodes.OK.rc):
            oldResult = result.message
            result = self.keyword_arguments["OnError"]
            result.message = oldResult

        return (result)
