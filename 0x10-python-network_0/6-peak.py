#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
    - list_of_integers: List of integers.

    Returns:
    - A peak element if found, otherwise None.
    """
    if list_of_integers == []:
        return None

    size = len(list_of_integers)

    if size == 1 or list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    elif list_of_integers[-1] >= list_of_integers[-2]:
        return list_of_integers[-1]

    mid = size // 2
    if list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid:])

#    if size == 1:
#        return list_of_integers[0]
#    elif size == 2:
#        return max(list_of_integers)
#
#    mid = int(size/2)
#    peak = list_of_integers[mid]
#
#    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
#        return peak
#    elif peak < list_of_integers[mid - 1]:
#        return find_peak(list_of_integers[:mid])
#    else:
#        return find_peak(list_of_integers[mid + 1:])
