#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        mod_string = my_string.replace("c", "").replace("C", "")
        return(mod_string)
