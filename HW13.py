#Preston
#5th Hour
#HW13


#1. Create a list containing 10 integers of your choice.

#2. Create two empty variables named evenNumbers and oddNumbers.

#3. Make a loop that counts the number of even and odd numbers in the list.
#(HINT: The way to see if a number is even is if it is divisible by 2).

# Print the total count of even and odd numbers.

numList = [1,2,3,4,5,6,7,8,9,10]
print (numList)

evenNumbers = 0
oddNumbers = 0

for i in numList:
    if i % 2 == 0:
        evenNumbers += 1
    else:
        oddNumbers += 1

print(evenNumbers)
print(oddNumbers)