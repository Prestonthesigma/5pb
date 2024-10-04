#Preston
#5th Hour
#HW6

print ("hello world")

number = 10
if number % 2 == 0:
    if number % 3 == 0:
        print(number/2)
        print(number/3)
    else:
        print("number is not divisible by 3.")
        print(number/2)
else:
    if number % 3 == 0:
        print("number is not divisible by 2.")
        print(number/3)
    else:
        print("number is divisible by neither 2 nor 3.")





#If num is divisible by 2
#   if num is divisible by 3
#       print the result of num being divided by 2
#       print the result of num being divided by 3
#   else
#       print that it is not divisible by 3
#       print the result of num being divided by 2
#else
#   if num is divisible by 3
#       print that num is not divisible by 2
#       print the result of num being divided by 3
#   else
#       print that neither is divisible by 2 or 3