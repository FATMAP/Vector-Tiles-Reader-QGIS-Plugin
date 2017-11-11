# -*- coding: utf-8 -*-
#
# This code is licensed under the GPL 2.0 license.
#
import unittest
import os
import sys
from qgis.core import *
from qgis.utils import iface
from PyQt4.QtCore import *

from test_mbtiles_source import MbtileSourceTests
from test_tilehelper import TileHelperTests
from test_vtreader import IfaceTests
from test_tilejson import TileJsonTests


def suites():
    return [
        unittest.makeSuite(MbtileSourceTests, 'test'),
        unittest.makeSuite(TileHelperTests, 'test'),
        unittest.makeSuite(IfaceTests, 'test'),
        unittest.makeSuite(TileJsonTests, 'test'),
    ]


# run all tests using unittest skipping nose or testplugin
def run_all():
    for s in suites():
        unittest.TextTestRunner(verbosity=3, stream=sys.stdout).run(s)


if __name__ == "__main__":
    run_all()