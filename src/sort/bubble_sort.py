# -*- coding: utf-8 -*-
from .. import utils

class BubbleSort():
    def __init__(self, array):
        self.array = array

    def sort(self):
        sorted = self.array.copy()
        swapped = True
        while swapped:
            swapped = False
            for i in range(1, len(sorted)):
                if sorted[i] < sorted[i-1]:
                    sorted = utils.array_swap_items(sorted, i-1, i)
                    swapped = True

        return sorted
