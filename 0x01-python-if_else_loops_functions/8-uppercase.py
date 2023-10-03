#!/usr/bin/python3

def uppercase(str):
    res = ''
    for char in str:
        if 'a' <= char <= 'z':
            upper = ord(char) - ord('a') + ord('A')
            res += chr(upper)
        else:
            res += char

    print("{}".format(res))
