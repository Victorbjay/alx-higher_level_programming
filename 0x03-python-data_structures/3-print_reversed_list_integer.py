#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        length = len(my_list)

        rev = my_list[length-1::-1]

        for i in rev:
            print("{:d}".format(i))
