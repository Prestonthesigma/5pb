#Name: Preston
#Class: 5th Hour
#Assignment: HW17

import random

#1. Import the "random" library and create a def function that prints "Hello World!"
def helloworld():
    print("Hello World!")

#2. Create two empty integer variables named "heads" and "tails"
heads = 0
tails = 0
#3. Create a def function that flips a coin one hundred times and increments the result in the above variables.
def coinflip():
    global heads, tails
    for i in range (1, 101):
        flip = random.randint (1,2)
        if flip == 1:
            heads += 1
        elif flip == 2:
            tails+= 1

#4. Call the "Hello world" and "Coin Flip" functions here
helloworld()
coinflip()
#5. Print the final result of heads and tails here
print (tails)
print (heads)
