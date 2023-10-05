#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    sum = add(a, b)
    dif = sub(a, b)
    mult = mul(a, b)
    dv = div(a, b)

print("{0} + {1} = {2}".format(a, b, sum))
print("{0} - {1} = {2}".format(a, b, dif))
print("{0} * {1} = {2}".format(a, b, mult))
print("{0} / {1} = {2}".format(a, b, dv))
