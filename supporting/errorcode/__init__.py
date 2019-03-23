##
# Errorcode object
# @Since: 22-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190322.0 - JBE - Initial

class Errorcode(object):
    # global variables
    className ='errorcode'
    def __init__(self, rc, code, message, resolution, area, level):
        self.rc=rc
        self.code=code
        self.message=message
        self.resolution=resolution
        self.area=area
        self.level=level
