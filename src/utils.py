# -*- coding: utf-8 -*-

def array_swap_items(input_array, index1, index2):
    """
    Swap 2 items in an array
    :param array: the array where items are swapped
    :param index1: element to swap
    :param index2: element to swap
    :return: the array with items swapped
    """
    output_array = input_array.copy()
    temp = output_array[index1]
    output_array[index1] = output_array[index2]
    output_array[index2] = temp
    return output_array
