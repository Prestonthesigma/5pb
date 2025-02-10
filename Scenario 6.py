#Name: Preston
#Class: 5th Hour
#Assigment: Scenario 6



import random


statblock = []
def roll_dice():
    for i in range (6):
        roll = [random.randint(1,6,), random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6),random.randint(1,6)]
        roll.sort(reverse=True)
        stat = roll[0] + roll [1] + roll[2] + roll [3] + roll [4] + roll [5]
        statblock.append(stat)

roll_dice()
print(statblock)
