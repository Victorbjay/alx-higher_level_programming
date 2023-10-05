#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    arg_len = len(args)

    total_sum = 0

    for i in range(arg_len):
        num = int(args[i])
        total_sum += num
print("{}".format(total_sum))
