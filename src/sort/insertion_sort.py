# -*- coding: utf-8 -*-
from .. import utils

class InsertionSort():
    def __init__(self, array):
        self.array = array

    def sort(self):
        sorted = self.array.copy()
        i = 1
        while i < len(sorted):
            j = i
            while j > 0 and sorted[j-1] > sorted[j]:
                sorted = utils.array_swap_items(sorted, j-1, j)
                j -= 1
            i += 1

        return sorted
