
import os
import shutil
import logging
import Settings as s
import time


# From https://stackoverflow.com/questions/15147713/python-log-to-multiple-log-files
def GetScheduleLogger():
    logger = logging.getLogger('SchedulerLogs')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s- %(message)s')
 
    RunStartTime = int(time.time())

    #to log debug messages                               
    debug_log = logging.FileHandler(os.path.join(s.LogsPath, 'debug_' + str(RunStartTime) +'.log'))
    debug_log.setLevel(logging.DEBUG)
    debug_log.setFormatter(formatter)

    #to log errors
    error_log = logging.FileHandler(os.path.join(s.LogsPath, 'error_' + str(RunStartTime) +'.log'))
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
 
    print("Writing logs to path : " + s.LogsPath)
    return(logger)


if __name__ == '__main__':
    writelogs = GetScheduleLogger()
  
    writelogs.debug('This message should go in the debug log')
  
    writelogs.info('and so should this message')
    writelogs.warning('and this message')
    writelogs.error('This message should go in both the debug log and the error log')

MyLogger = GetScheduleLogger()
