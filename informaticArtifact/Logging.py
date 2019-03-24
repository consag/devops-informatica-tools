
import os
import logging
import supporting.settings as s
import time


# From https://stackoverflow.com/questions/15147713/python-log-to-multiple-log-files
def getArtifactLogger():
    logger = logging.getLogger('artifactLogs')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s- %(message)s')
 
    RunStartTime = int(time.time())

    #to log debug messages                               
    debug_log = logging.FileHandler(os.path.join(s.logDir, 'debug_' + str(RunStartTime) +'.log'))
    debug_log.setLevel(logging.DEBUG)
    debug_log.setFormatter(formatter)

    #to log errors
    error_log = logging.FileHandler(os.path.join(s.logDir, 'error_' + str(RunStartTime) +'.log'))
    error_log.setLevel(logging.ERROR)
    error_log.setFormatter(formatter)

    #to log console outputs
    console_output = logging.StreamHandler()
    # console_output.setLevel(logging.WARNING)
    console_output.setLevel(logging.INFO)
    console_output.setFormatter(formatter)

    logger.addHandler(debug_log)
    logger.addHandler(error_log)
    logger.addHandler(console_output)
 
    print("Writing logs to path : " + s.logDir)
    return(logger)


if __name__ == '__main__':
    writelogs = getArtifactLogger()

MyLogger = getArtifactLogger()
