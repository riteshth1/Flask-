## Functions can have inputs/functionality/output
def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.

# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)
#
# result = calculate(add, 2, 3)
# print(result)

##Functions can be nested in other functions

# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     nested_function()
#
# outer_function()

## Functions can be returned from other functions
# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     return nested_function
#
# inner_function = outer_function()
# inner_function

## Decorator function
"""
it's an functions that wraps another function and gives that function another functionality.
A decorator is a design pattern in Python that allows a user to add new functionality to an
existing object without modifying its structure.    
"""

import time

def delay_decorator(function):
    def wrapped_function():
        time.sleep(3)
        # Do something before
        function()
        function()
        #do something after
    return  wrapped_function

@delay_decorator
def say_hello():
    print("hello")

@delay_decorator
def say_bye():
    print("bye")

def greetings():
    print("Good Morning!..")

# Note: @ is known as syntactic sugar
say_hello()
say_bye()