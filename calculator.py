# https://github.com/hamzabaig0/lab10-HB-WR.git
# Partner 1: Hamza Baig
# Partner 2: Wilfredo Rodriguez

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math


def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError as e:
        print(f"Cannot take square root of a negative number.")


def hypotenuse(a, b):
    try:
        return math.hypot(a, b)  # can have negative nums
    except ValueError as e:
        print(f"Neither sides can equal 0")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a


def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Base 'a' must be positive and not equal to 1.")
    if b <= 0:
        raise ValueError("Argument 'b' must be positive.")
    return math.log(b, a)
