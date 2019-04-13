# -*- coding: utf-8 -*-

from .context import src

import unittest


class UtilsTestSuite(unittest.TestCase):

    def test_array_swap_items(self):
        array = [0, 1, 2, 3, 4]
        index1 = 1
        index2 = 3
        swapped_array = [0, 3, 2, 1, 4]
        self.assertListEqual(src.utils.array_swap_items(array, index1, index2), swapped_array)
