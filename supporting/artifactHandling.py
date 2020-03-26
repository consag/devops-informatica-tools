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
import supporting.generalConstants as constants
import logging, os, datetime
import supporting

# import repositorytools

now = datetime.datetime.now()
result = err.OK

logger = logging.getLogger(__name__)
workspace = constants.DEFAULT_WORKSPACE


def get_artifact(artifact_name):
    thisproc = "get_artifact"
    global workspace
    # something like this:    artifact = repositorytools.Artifact("group","demoArtifact","1.0.0","classifier","zip")
    # at the moment cicd runs in Azure DevOps and artifacts are stored within the pipeline.

    workspace = get_workspace()
    supporting.log(logger, logging.DEBUG, thisproc, 'workspace is >' + workspace + "<.")

    return workspace + "/" + artifact_name


def get_workspace():
    return os.environ.get(constants.varWorkspace, constants.DEFAULT_WORKSPACE)


def store_artifact(artifact_name):
    thisproc = "store_artifact"
    return err.NOT_IMPLEMENTED
