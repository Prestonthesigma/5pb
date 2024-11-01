#Preston
#Class: 5th Hour
#Assignment: HW11

#A common exercise in computer science is "FizzBuzz". The rules of
#the game are simple. Count from 1 to 100 but with every number that
#is divisible by 3 you say "Fizz" instead of the number,
#every number divisible by 5 you say "Buzz" instead,
#and if it's divisible by both you say "FizzBuzz".

#Create a while loop that follows the rules of the game.
#(HINT: Look back to HW6 on how to see if a number is divisible by another)


MAXVAL = 100
i = 1
while (i < MAXVAL+1):
    if i % 3 == 0 and i % 5 == 0:
        print(i, 'fizzbuzz')
    # If the number is divisible by 3, print the word bar
    elif i % 3 == 0:
        print(i, 'fizz')
    #If the number is divisible by 5, print the word baz
    elif i % 5 == 0:
        print(i, 'buzz')
    i += 1

#credit:https://python-forum.io/thread-38236.html