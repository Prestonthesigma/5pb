#Preston
#5th Hour
#HW12

#1. Create a for loop with variable i that counts down from 5 to 1
#and then prints "Hello World!" at the end.

#2. Create a for loop that counts up and prints only even numbers
#between 1 and 30.
#(HINT: Look back to HW6 on how to see if a number is divisible by another)

#3. Create a for loop that prints 5 different animals from a list.

#4. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")


for i in range (1, 6) [::-1]:
    print (i)
print("hello world")

for i in range (2, 31, 2):
    print(i)

animals = ["dog", "monkey", "gorilla","Hank", "Bird"]

for y in animals:
    print(y)

for w in input("choose a word!") [::-1]:
    print(w)