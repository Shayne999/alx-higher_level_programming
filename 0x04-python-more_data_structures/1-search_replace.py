#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replacement = list(map(lambda x: x if x == search else x, my_list))
    return (replacement)
