# -*- coding: utf-8 -*-

from .context import src

import unittest
import random


class SortTestSuite(unittest.TestCase):
    sorted_array = [0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
    random_array = sorted_array.copy()
    random.shuffle(random_array)

    def test_bubble_sort(self):
        self.assertListEqual(src.BubbleSort(self.random_array).sort(), self.sorted_array)

