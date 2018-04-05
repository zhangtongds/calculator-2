"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

def calculator():
    while True:
        user_input = raw_input("Please enter operator command, number(s) you want to calculate.")
        token = user_input.split(" ")
        if token[0] == "q":
            return
        else:
            print calculation(token)
def calculation(token):   
    if token[0] != "q":
        if token[0] == "+":
            return add(int(token[1]), int(token[2]))
        if token[0] == "-":
            return subtract(int(token[1]), int(token[2]))
        if token[0] == "*":
            return multiply(int(token[1]), int(token[2]))
        if token[0] == "/":
            return divide(int(token[1]), int(token[2]))
        if token[0] == "square":
            return square(int(token[1]))
        if token[0] == "cube":
            return cube(int(token[1]))
        if token[0] == "pow":
            return power(int(token[1]), int(token[2]))
        if token[0] == "mod":
            return mod(int(token[1]), int(token[2]))
    else:
        print("You have exited the calculator.")    