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
# General constants for build and deploys
# @Since: 22-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190410.0 - JBE - Initial

##
# Environment variable values
##
# Generic
varLogDir ='LOGDIR'
DEFAULT_LOGDIR = '.'
varResultDir ='RESULTDIR'
DEFAULT_RESULTDIR = '.'
varArtifactDir ='ARTIFACTDIR'
DEFAULT_ARTIFACTDIR = '.'
varConfigDir = 'CONFIGDIR'
DEFAULT_CONFIGDIR = '.'
varSourceDir = 'SOURCEDIR'
DEFAULT_SOURCEDIR = '.'

##
# pipeline
varWorkspace = 'PIPELINE_WORKSPACE'
DEFAULT_WORKSPACE = '.'

##
# Release
varReleaseId = 'BUILD_BUILDNUMBER'

##
#
NOT_SET = 'NotSet'
YES = 'Yes'
NO = 'No'
TRUE = "True"
FALSE = "False"

##
# Environment defaults
# If not set on command line (if supported) and not as environment variable
DEFAULT_RELEASEID = '0.1'

# Nexus
varGroupId = "General"
