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
