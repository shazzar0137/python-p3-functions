#!/usr/bin/env python3

def greet_programmer():
    pass
    print("Hello, programmer!")

def greet(name):
    pass
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    pass
    print(f"Hello, {name}!")

def add(num1, num2):
    pass
    return num1 + num2

def halve(number):
    pass
    if (type(number) == int or type(number) == float):
        return number / 2
    else:
        return None
