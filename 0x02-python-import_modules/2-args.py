#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    args_num = len(args)

    if args_num == 0:
        print("{} arguments.".format(args_num))
    elif args_num == 1:
        print("{} argument:".format(args_num))
    else:
        print("{} arguments:".format(args_num))

    for i in range(args_num):
        print("{}: {}".format(i + 1, args[i]))
