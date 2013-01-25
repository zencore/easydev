# -*- python -*-
# -*- coding: utf-8 -*-
#
#  This file is part of the easydev software
#
#  Copyright (c) 2011-2013 
#
#  File author(s): Thomas Cokelaer <cokelaer@gmail.com>
#
#  Distributed under the GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
#  Website: https://www.assembla.com/spaces/pyeasydev/wiki
#  Documentation: http://packages.python.org/easydev
#
##############################################################################
# $:Id $
"""toolkit to ease development"""
import os
import subprocess
import tempfile
from os.path import join as pj
import glob
import time


__all__ = ["shellcmd", "checkParam"]


def checkParam(param, valid_values):
    """Checks that the value of param is amongst valid

    :param param: a parameter to be checked
    :param list valid_values: a list of values 

    ::

        checkParam(1, [1,2,3])
        checkParam(mode, ["on", "off"])
    """
    if isinstance(valid_values, list) == False:
        raise TypeError("the valid_values second argument must be a list of valid values")

    if param not in valid_values:
        msg = "Incorrect value provided (%s)" % param
        msg += "    Correct values are %s" % valid_values
        raise ValueError(msg)
    

def shellcmd(cmd, show=True, verbose=False):
    """An alias to run system commands.

    Based on subprocess.

    :param cmd: the command to call
    :param show: print the command
    :param verbose: print the output

    :return: the output
    """
    if show:
        print(cmd)
    try:
        ret = subprocess.Popen([cmd], stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, shell=True)
        ret.wait()

        output = ret.stdout.read().strip()
        error = ret.stderr.read().strip()

        if len(error)>0:
            raise Exception(error)

        if verbose == True:
            print output

        return output
    except Exception, e:
        #if verbose: print e
        raise Exception("Error:: Command (%s) failed. Error message is %s" % (cmd, e))



