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
import supporting.errorcodes as err
from zipfile import ZipFile
import os
import logging
import supporting
import fnmatch

logger = logging.getLogger(__name__)


def generate_zip(basedirectory, directory, zipFileName, filter='*', suppress_extension='7Al!#%ˆˆ'):
    thisproc = "generate_zip"

    supporting.log(logger, logging.DEBUG, thisproc,
                   "Creating new zip >" + zipFileName + "<...")
    # create a ZipFile object
    with ZipFile(zipFileName, 'w') as zipObj:
        additemto_zip(zipObj, basedirectory, directory, filter, suppress_extension)
    supporting.log(logger, logging.DEBUG, thisproc,
                   "Done.")

    return err.OK


def addto_zip(basedirectory, directory, zipFileName, filter='*', suppress_extension='7Al!#%ˆˆ'):
    thisproc = "addto_zip"

    supporting.log(logger, logging.DEBUG, thisproc,
                   "Adding to zip >" + zipFileName + "<...")

    # create a ZipFile object
    with ZipFile(zipFileName, 'a') as zipObj:
        additemto_zip(zipObj, basedirectory, directory, filter, suppress_extension)

    supporting.log(logger, logging.DEBUG, thisproc,
                   "Done.")

    return err.OK


def additemto_zip(zipObj, basedirectory, item, filter='*', suppress_extension='7Al!#%ˆˆ'):
    thisproc = "additemto_zip"

    supporting.log(logger, logging.DEBUG, thisproc,
                   "Adding >" + item + "< ...")

    for folderName, subfolders, filenames in os.walk(item):
        for filename in filenames:
            if filename.endswith('.' + suppress_extension):
                supporting.log(logger, logging.DEBUG, thisproc,
                               "Ignoring >" + filename + "< as it has the extension >" + suppress_extension + "<.")
            else:
                if fnmatch.fnmatch(filename, filter):
                    filePath = os.path.join(folderName, filename)
                    # Add file to zip
                    archive_name = filePath[len(basedirectory):]
                    supporting.log(logger, logging.DEBUG, thisproc,
                                   "Adding >" + filePath + "< to zip as >" + archive_name + "<.")
                    zipObj.write(filePath, archive_name)
                else:
                    supporting.log(logger, logging.DEBUG, thisproc,
                                   ">" + filename + "< was not added to zip as it does not match pattern >" + filter + "<.")

    supporting.log(logger, logging.DEBUG, thisproc,
                   "Done adding >" + item + "< ...")

    return err.OK
