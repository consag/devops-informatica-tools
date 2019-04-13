import logging, supporting
import supporting.errorcodes as err

logger = logging.getLogger(__name__)
deployItems = []

def getWorkitemList(deployList):
    thisproc = "processList"
    latestError = err.OK
    global entrynr
    entrynr = 0
    global level
    supporting.log(logger, logging.DEBUG, thisproc, "Started to work on deploy list >" + deployList + "<.")

    try:
        with open(deployList) as theList:
            for line in theList:
                entrynr += 1
                if line.startswith("#"):
                    supporting.log(logger, logging.DEBUG, thisproc, "Ignoring comment line >" + str(entrynr) + "<.")
                else:
                    line = line.rstrip('\n')
                    if line:
                        deployItems.append(line)
                        supporting.log(logger, logging.DEBUG, thisproc, "line >" + str(entrynr) +"< added to worklist.")
                    else:
                        supporting.log(logger, logging.DEBUG, thisproc, "Ignoring empty line >" + str(entrynr) +"<.")
    except IOError:
        supporting.log(logger, logging.ERROR, thisproc, "File not found")
        latestError = err.FILE_NF

    supporting.log(logger, logging.DEBUG, thisproc,
                   "Completed with rc >" + str(latestError.rc) + "< and code >" + latestError.code + "<.")
    return latestError, deployItems
