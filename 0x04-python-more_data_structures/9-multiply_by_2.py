#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiplied = a_dictionary.copy()
    list_key = list(multiplied.keys())

    for i in list_key:
        multiplied[i] *= 2
    return (multiplied)
