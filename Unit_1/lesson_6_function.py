# function
# Standard Library Function original
# Programmer Defined Function


# Standard Library Function
# from math import sqrt
# import math
# data = int(input("Please enter a number to sqrt: "))
# print(f"The square root of {data} is: {math.sqrt(data)}")
# print("The value of pi is", math.pi)
# print(f"The exp of {data} is: {math.exp(data)}")
# print(f"the hex value of {data} is: {hex(data)}")


# Programmer Defined Function

def add(a, b):  # function header a,b = parameters
    return a + b  # Function body
  # function calling


def sub(a, b):
    return a - b


def multiply(c, d):
    return c * d


def divide(e, f):
    if f == 0:
        return "Cannot divided by 0"
    return e / f


fdata = float(input("Please enter first number: "))
sdata = float(input("Please enter second number: "))

print(f'adding {add(fdata,sdata)}')
print(f'subtract {sub(fdata, sdata)}')
print(f'Multiply {multiply(fdata, sdata)}')
print(f'dividing {divide(fdata,sdata)}')
