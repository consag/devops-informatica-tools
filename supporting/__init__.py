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

    ResultDir = os.environ.get(constants.varResultDir, '.')
    ResultFileName = ResultDir + "/" + now.strftime("%Y%m%d-%H%M%S.%f") + '.' + '.result'

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

    return


def log(logger, level, area, message):

    logger.log(level, area + " - " + message)
    return

def writeresult2(resultlogger, result):
    resultlogger.info('RC=' +str(result.rc) +'\n')
    resultlogger.info('CODE=' + result.code + '\n')
    resultlogger.info('MSG=' + result.message + '\n')
    resultlogger.info('RESOLUTION=' + result.resolution + '\n')
    resultlogger.info('AREA=' + result.area + '\n')
    resultlogger.info('ERRLEVEL=' + str(result.level) + '\n')


def writeresult(result):
    ResultDir = os.environ.get(constants.varResultDir, '.')
    ResultFileName = ResultDir + "/" + now.strftime("%Y%m%d-%H%M%S.%f") + '.' + '.result'

    with open(ResultFileName, 'w') as the_result_file:
        the_result_file.write('RC=' + str(result.rc) + '\n')
        the_result_file.write('CODE=' + result.code + '\n')
        the_result_file.write('MSG=' + result.message + '\n')
        the_result_file.write('RESOLUTION=' + result.resolution + '\n')
        the_result_file.write('AREA=' + result.area + '\n')
        the_result_file.write('ERRLEVEL=' + str(result.level) + '\n')
    return


def exitscript(result):
    thisProc = "exitscript"
    log(logging.ERROR, thisProc, result.area +
        ' exit requested. Return code >' + str(result.rc) + "< and code >" + result.code + "<.")
    writeresult(result)
    raise SystemExit

#configurelogger()
