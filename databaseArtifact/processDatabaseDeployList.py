import supporting.errorcodes as err
import supporting, logging

def processEntry(deployEntry):
    thisProc="processEntry"
    result = err.OK
    supporting.log(logging.DEBUG, thisProc, "Started to work on deploy entry >" + deployEntry +"<.")


    supporting.log(logging.DEBUG, thisProc, "Completed with rc >" + str(result.rc) +"< and code >" +result.code +"<.")
    return err.OK

def processList(deployList):
    thisProc="processList"
    latestError = err.OK
    supporting.log(logging.DEBUG, thisProc, "Started to work on deploy list >" + deployList +"<.")

    try:
        with open(deployList) as theList:
            for line in theList:
                result = processEntry(line)
                if(result.rc != err.OK.rc):
                    latestError = result
    except IOError:
        supporting.log(logging.ERROR, thisProc, "File not found")

    supporting.log(logging.DEBUG, thisProc, "Completed with rc >" + str(latestError.rc) +"< and code >" +latestError.code +"<.")
    return latestError

