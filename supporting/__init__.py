##
# Supporting modules
# @Since: 22-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190412.0 - JBE - Initial

import logging, datetime, os
import supporting.generalConstants as constants

now = datetime.datetime.now()


def configurelogger(mainProc):

    logdir = os.environ.get(constants.varLogDir, constants.DEFAULT_LOGDIR)
    logging.basicConfig(filename= logdir +"/" + now.strftime("%Y%m%d-%H%M%S.%f") + '-' + mainProc + '.log'
                        , level=logging.DEBUG
                        , format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    ResultDir = os.environ.get(constants.varResultDir, constants.DEFAULT_RESULTDIR)
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
    thisProc = "exitscript"
    log(logging.ERROR, thisProc, result.area +
        ' exit requested. Return code >' + str(result.rc) + "< and code >" + result.code + "<.")
    writeresult(resultlogger, result)
    raise SystemExit


