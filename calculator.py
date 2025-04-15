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
# calculator.py
# Defines functions used to create a simple calculator
# One function per operation, in order.

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)  # Accepts 0 or negative values, no error needed

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Base 'a' must be positive and not equal to 1.")
    if b <= 0:
        raise ValueError("Argument 'b' must be positive.")
    return math.log(b, a)

def exp(a, b):
    return a**b