#Preston
#5th Hour
#HW15
import random
import inspect


#1. Create a def function that prints out "Hello World!"
def hello_world():
    print("Hello World")
hello_world()
#2. Create a def function that calculates the average of three numbers.

#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.

#4. Create a def function that loops from 1 to the number put in the argument.

#5. Call all of the functions created in 1 - 4 with relevant arguments.

def average(num_one, num_two, num_three):
  avg = (int(num_one) + int(num_two) + int(num_three))/3
  return avg

num_one = input()
num_two = input ()
num_three = input ()
print(average(num_one, num_two,num_three))

def animal_list(*animal):
    print("the third animal is", animal[2])
animal_list("hippo", "Hank", "dog", "guinea pig","zebra")

def loop_to_number(n):
  for i in range(1, n + 1):
    print(i)

loop_to_number(9)
