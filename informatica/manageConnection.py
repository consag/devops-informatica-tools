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
from informatica import buildCommand
from informatica import executeInfacmd
from supporting import errorcodes

logger = logging.getLogger(__name__)
entrynr =0

def create_connection(**KeyWordArguments):
    thisproc = "create_connection"

    KeyWordArguments["Tool"] = "CreateConnection"
    RunCommand = buildCommand.build(**KeyWordArguments)

    log(logger, logging.INFO, thisproc, "RunCommand is >" + RunCommand + "<.")
    result = executeInfacmd.execute(RunCommand)

    if(result.code == errorcodes.INFACMD_FAILED):
        oldResult = result.message
        result = errorcodes.INFACMD_PROFILE_FAILED
        result.message = oldResult

    return (result)


def delete_connection(**KeyWordArguments):
    thisproc = "delete_connection"

    KeyWordArguments["Tool"] = "DeleteConnection"
    RunCommand = buildCommand.build(**KeyWordArguments)

    log(logger, logging.INFO, thisproc, "RunCommand is >" + RunCommand + "<.")
    result = executeInfacmd.execute(RunCommand)

    if(result.code == errorcodes.INFACMD_FAILED):
        oldResult = result.message
        result = errorcodes.INFACMD_PROFILE_FAILED
        result.message = oldResult

    return (result)


def update_connection(**KeyWordArguments):
    thisproc = "update_connection"
    """Usage:
        <-DomainName|-dn> domain_name
        <-UserName|-un> user_name
        <-Password|-pd> password
        [<-SecurityDomain|-sdn> security_domain]
        [<-ResilienceTimeout|-re> timeout_period_in_seconds]
        <-ConnectionName|-cn> connection_name
        [<-ConnectionUserName|-cun> connection_user_name]
        [<-ConnectionPassword|-cpd> connection_password]
        <-Options|-o> options, separated by space in the form of name=value.  Use single quote to escape any equal sign or space in the value.

    Updates a connection. To list connection options, run infacmd isp ListConnectionOptions.
    """

    KeyWordArguments["Tool"] = "UpdateConnection"
    RunCommand = buildCommand.build(**KeyWordArguments)

    log(logger, logging.INFO, thisproc, "RunCommand is >" + RunCommand + "<.")
    result = executeInfacmd.execute(RunCommand)

    return (result)


def list_connection_options(**KeyWordArguments):
    thisproc = "list_connection_options"

    KeyWordArguments["Tool"] = "ListConnectionOptions"
    RunCommand = buildCommand.build(**KeyWordArguments)

    log(logger, logging.INFO, thisproc, "RunCommand is >" + RunCommand + "<.")
    result = executeInfacmd.execute(RunCommand)

    return (result)

