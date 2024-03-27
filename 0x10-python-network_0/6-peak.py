#!/usr/bin/python3
"""Algorithm for list of integers."""


def find_peak(list_of_integers):
    """Finds the  peak in a list of unsorted integer values."""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
