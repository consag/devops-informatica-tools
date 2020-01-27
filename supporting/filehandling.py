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

##
# File handling
# @Since: 23-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190323.0 - JBE - Initial

import contextlib, os, shutil


def removefile(filename):
    with contextlib.suppress(FileNotFoundError):
        os.remove(filename)


def copy_file(source, target):
    with contextlib.suppress(FileExistsError):
        shutil.copy2(source, target)

def copy_files(source, target):
    with contextlib.suppress(FileExistsError):
        for file in os.listdir(source):
            shutil.copy2(source + '/' + file, target)

def create_directory(directory):
    os.makedirs(directory, exist_ok=True)  # succeeds even if directory exists.
