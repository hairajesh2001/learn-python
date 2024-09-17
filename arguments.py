#!/usr/bin/env python
import sys
print("Welcome to Python Learing ")


def add():
    sub_result = int(number1) + int(number2)
    return sub_result
    

number1 = sys.argv[1]
number2 = sys.argv[3]
operator = sys.argv[2]

if operator == "add":
    output = add(number1,number2)
    print()



