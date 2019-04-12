import supporting.errorcodes as err
import logging, supporting

logger = logging.getLogger(__name__)
deployItems = []

def getWorkitemList(deployList):
    thisproc = "processList"
    latestError = err.OK
    global entrynr
    entrynr = 0
    global level
    level = 0
    supporting.log(logger, logging.DEBUG, thisproc, "Started to work on deploy list >" + deployList + "<.")

    try:
        with open(deployList) as theList:
            for line in theList:
                entrynr += 1
                level = 0
                deployItems.append( line.rstrip('\n'))
    except IOError:
        supporting.log(logger, logging.ERROR, thisproc, "File not found")
        latestError = err.FILE_NF

    supporting.log(logger, logging.DEBUG, thisproc,
                   "Completed with rc >" + str(latestError.rc) + "< and code >" + latestError.code + "<.")
    return latestError, deployItems
