#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_elements = set(my_list)
    num = 0

    for _ in unique_elements:
        num += 1
    return (num)
