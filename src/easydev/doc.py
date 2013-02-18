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
"""Module related to documentation


.. testsetup::

    from easydev.doc import *

"""
__all__ = ["underline"]

def underline(text, symbol="="):
    """Underlines a string with a specific character

    :param str text: the text to underline
    :param str symbol: the character to be used to underline the text
    :return: underlined text.

    .. doctest::

        >>> print(underline("test"))
        test
        ====

    """
    l = len(text)
    return text + "\n" + l * symbol

