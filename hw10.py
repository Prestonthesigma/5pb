#Preston
#5th Hour
#HW10

#Name:
#Class: 5th Hour
#Assignment: HW10

#1. Create a while loop with variable i that counts down from 5 to 0
#and then prints "Hello World!" at the end.

#2. Create a while loop that prints only even numbers
#between 1 and 30.

#3. Create a while loop that repeats until the user
#inputs the number 0.


import time

x = 5

while True:
    print(x)
    time.sleep(0.4)
    x -= 1
    if x == 0:
        print("Hello World!")
        break

i = 0
while i <=30:
 print(i)
 time.sleep(0.2)
 i += 2

y = int(input("Enter a number"))

while y != 0:
    y=int(input("enter a different number"))

