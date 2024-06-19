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

    # Print results in the specified format
    print(f"{a} + {b} = {result_add}")
    print(f"{a} - {b} = {result_sub}")
    print(f"{a} * {b} = {result_mul}")
    print(f"{a} / {b} = {result_div}")
