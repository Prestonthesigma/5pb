#Name: Preston B
#Class: 5th Hour
#Assignment: HW20
from xml.etree.ElementTree import ParseError

#1. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.
try:
    print(x)
except:
    print("hello world")
#2. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.
try:
    num1 = 100
    num2 = int(input("number 2:"))
    division = num1 / num2
except ZeroDivisionError:
    print("can't divide by zero!")

#3. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.
try:
    numberPick = int(input("pick a number:"))
    print (numberPick)
except ValueError:
    print("not a number!")

#4. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.
x = 5

while True:
    print(x)
    x -= 1
    if x < 0:
        raise Exception("Sorry, no numbers below 0!")