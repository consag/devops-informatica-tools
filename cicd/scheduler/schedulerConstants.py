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
# Constants for Scheduler artifacts and deploys
# @Since: 25-OCT-2019
# @Author: Jac. Beekers
# @Version: 20191025.0 - JBE - Initial

# Scheduler artifacts
varSchedulerDeployList='SCHEDULER_DEPLOYLIST'
varSourceSchedulerDir='SOURCE_SCHEDULERDIR'
varSourceSchedulerTypeDir='SOURCE_SCHEDULER_TYPEDIR'
varTargetSchedulerDir='TARGET_SCHEDULERDIR'
varTargetSchedulerTypeDir='TARGET_SCHEDULER_TYPEDIR'
# Source is Git
varSchedulerGitRepo='SCHEDULER_GIT_REPOSITORY'
varSchedulerGitBranch='SCHEDULER_GIT_BRANCH'
varSchedulerPath='SCHEDULER_PATH'

##
# Scheduler artifact defaults
# Source is deploylist
DEFAULT_SOURCE_SCHEDULERDIR ='.'
DEFAULT_SOURCE_SCHEDULER_TYPEDIR ='.'
DEFAULT_TARGET_SCHEDULERDIR ='.'
DEFAULT_TARGET_SCHEDULER_TYPEDIR ='.'
DEFAULT_SCHEDULER_DEPLOYLIST ='scheduler_deploylist.txt'

NOT_SET ='NOT_SET'
##
# Airflow
PLUGINS = 'plugins'
DAGS = 'dags'
##
# Control-M
JOBTYPE = 'jobtype'
JOBASCODE = 'jobascode'
