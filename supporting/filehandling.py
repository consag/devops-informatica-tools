##
# File handling
# @Since: 23-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190323.0 - JBE - Initial

import contextlib, os

def removefile(filename):
    with contextlib.suppress(FileNotFoundError):
        os.remove(filename)
