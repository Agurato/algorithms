# -*- coding: utf-8 -*-

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
                    tmp = sorted[i]
                    sorted[i] = sorted[i-1]
                    sorted[i-1] = tmp
                    swapped = True


        return sorted
