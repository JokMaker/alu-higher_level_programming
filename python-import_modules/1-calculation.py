#!/usr/bin/python3


# 1-calculation.py

# Define variables a and b
a = 10
b = 5

# Import functions from calculator_1.py
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    # Perform calculations using imported functions
    result_add = add(a, b)
    result_sub = sub(a, b)
    result_mul = mul(a, b)
    result_div = div(a, b)

    # Print results in the specified format using .format()
    print("{0} + {1} = {2}".format(a, b, result_add))
    print("{0} - {1} = {2}".format(a, b, result_sub))
    print("{0} * {1} = {2}".format(a, b, result_mul))
    print("{0} / {1} = {2}".format(a, b, result_div))
