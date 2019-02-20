digitList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '.']
operatorList = ['+', '-', '/', '*', '^']
keyPressList = ['i', 'I', 'c', 'C', 'r', 'R', 'm', 'M', 's', 'S', 'x', 'X']

def buildNum (num):
     return num

def add (x, y, op):
    return x+y

def subtract (x,y,op):
    return x-y

def multiply (x,y, op):
    return x*y

def divide (x,y, op):
    if y != 0:
     return x/y
    else: 
     return ("Broken Universe: Division by zero.")

def power (x, y, op):
    return x**y

def invert (x):
     return (-1*x)

def memClear(x):
     x = 0
     return ("Memory Cleared.")   

def memRecall (x, memValue):
     x = memValue
     return memValue

def memStore (x, memValue):
     memValue = x
     return ("Value Stored.")
