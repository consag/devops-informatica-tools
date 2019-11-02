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
# Supporting modules
# @Since: 22-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190414.0 - JBE - Initial

import logging, datetime, os
import supporting.generalConstants as generalConstants
import supporting
import sys

logger = logging.getLogger(__name__)

now = datetime.datetime.now()


def configurelogger(mainProc, console=True):

    logdir = os.environ.get(generalConstants.varLogDir, generalConstants.DEFAULT_LOGDIR)
    logging.basicConfig(filename= logdir +"/" + now.strftime("%Y%m%d-%H%M%S.%f") + '-' + mainProc + '.log'
                        , level=logging.DEBUG
                        , format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # nice for Azure DevOps, but not for Airflow
    if console:
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # tell the handler to use this format
        console.setFormatter(formatter)
        # add the handler to the root logger
        logging.getLogger('').addHandler(console)


    ResultDir = os.environ.get(generalConstants.varResultDir, generalConstants.DEFAULT_RESULTDIR)
    ResultFileName = ResultDir + "/" + now.strftime("%Y%m%d-%H%M%S.%f") + '-' + mainProc + '.result'

    resultlogger = logging.getLogger('result_logger')
    resultlogger.setLevel(logging.INFO)
    # create file handler which logs even debug messages
    fh = logging.FileHandler(ResultFileName)
    fh.setLevel(logging.INFO)
    # create formatter and add it to the handler
    formatter = logging.Formatter('%(message)s')
    fh.setFormatter(formatter)
    # add the handlers to logger
    resultlogger.addHandler(fh)

    return resultlogger


def log(logger, level, area, message):

    logger.log(level, area + " - " + message)
    return

def writeresult(resultlogger, result):
    resultlogger.info('RC=' +str(result.rc) )
    resultlogger.info('CODE=' + result.code )
    resultlogger.info('MSG=' + result.message )
    resultlogger.info('RESOLUTION=' + result.resolution )
    resultlogger.info('AREA=' + result.area )
    resultlogger.info('ERRLEVEL=' + str(result.level) )


def exitscript(resultlogger, result):
    writeresult(resultlogger, result)
    sys.exit(result.rc)


def logentireenv():
    thisproc = "logentireenv"
    for param in os.environ.keys():
        supporting.log(logger, logging.DEBUG, thisproc,"%30s %s" % (param, os.environ[param]))

