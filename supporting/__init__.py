##
# Supporting modules
# @Since: 22-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190410.0 - JBE - Initial

import logging, datetime, os
import supporting.constants as constants
import databaseArtifact
import supporting.constants as constants


def configurelogger():
    now = datetime.datetime.now()
    logdir = os.environ.get(env.varLogDir, constants.DEFAULT_LOGDIR)
    logfilename = logdir + "/" + now.strftime("%Y%m%d-%H%M%S.%f") + '.' + 'databaseArtifact.log'
    # logger = logging.getLogger('build-and-deploy')
    logger = logging.getLogger()
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')

    if ( logdir is None ):
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    else:
        logfilename = logdir + "/" + now.strftime("%Y%m%d-%H%M%S.%f") + '.' + '.log'
        # logger = logging.getLogger('build-and-deploy')
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(logfilename)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    databaseArtifact.configDone = 1
    return


def log(level, area, message):
    if (databaseArtifact.configDone == 0):
        configurelogger()

    databaseArtifact.configDone = 1
    logging.getLogger(area)
    logging.log(level, area + ": " + message)
    return


def writeresult(result):
    now = datetime.datetime.now()
    ResultDir = os.environ.get(constants.varResultDir, '.')
    ResultFileName = ResultDir + "/" + now.strftime("%Y%m%d-%H%M%S.%f") + '.' + 'databaseArtifact.result'

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
