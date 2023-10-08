#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    length = len(my_list) - 1
    if idx < 0 or idx > length:
        return my_list
    for i in range(length + 1):
        if i == idx:
            my_list.remove(my_list[i])
    return my_list
