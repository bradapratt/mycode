#!/usr/bin/env python3
# Author: Bradley Pratt
# Created: 01/06/2021
# Last Edit: 01/06/2021

# ########GLOBAL VARIABLES##########
welcomeMessage = "Welcome to my python-based calculator! Current performable operations: ADD, SUBTRACT, MULTIPLY, " \
                 "DIVIDE. "
operators = {'+', '-', '*', '/'}
result = 0


# ########MAIN FUNCTION##########
def main():
    print(welcomeMessage)

    num1 = input("Enter your first operand: ")
    num1 = validateNum(num1)

    op = input("Enter the operator ( + | - | * | / ): ")
    op = validateOp(op)

    num2 = input("Enter your second operand: ")
    num2 = validateNum(num2)

    performOperation(num1, num2, op)

    print(num1, op, num2, "=", result, sep=" ")


# ########ACCESSORY FUNCTION##########
def validateNum(num):
    while True:
        try:
            num = float(num)
            return num
        except ValueError:
            num = input("That's not a valid number! Try again: ")


def validateOp(operator):
    while True:
        if operator in operators:
            return operator
        else:
            operator = input("That's not a valid operator! Try again: ")


def performOperation(num1, num2, op):
    global result
    if op == "+":
        result = add(num1, num2)
    elif op == "-":
        result = add(num1, -num2)
    elif op == "*":
        result = multiply(num1, num2)
    else:
        result = multiply(num1, 1/num2)


def add(first, second):
    return first + second


def multiply(first, second):
    return first * second


# Call the main function
main()

