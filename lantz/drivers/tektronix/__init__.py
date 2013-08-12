# -*- coding: utf-8 -*-
"""
    lantz.drivers.tektronix
    ~~~~~~~~~~~~~~~~~~~~~~~

    :company: Tektronix.
    :description: Test and Measurement Equipment.
    :website: http://www.tek.com/

    ---

    :copyright: 2012 by Lantz Authors, see AUTHORS for more details.
    :license: BSD,

"""

from .tds2024b import TDS2024
from .tds1002b import TDS1002b

__all__ = ['TDS2024', 'TDS1002b']

