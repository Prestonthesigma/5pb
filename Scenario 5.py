#Name: Preston and Eli
#Class: 5th Hour
#Assignment: Scenario 5

#Scenario 5
#You're all part of a new development team and the big wigs want to see what you are all capable of.
#They want you to develop whatever you want to develop, but there's only one problem:
#the same big wigs only bought enough computers for half of you. Because of this, you will
#all be split into teams of two. One serving as the brain (not using the computer),
#one serving as the hands (using the computer).

#The Teams are as such:

#Team 1: Dom (brain), Zachary (hand)
#Team 2: Ryley (brain), Ethan W (hand)
#Team 3: Eli (brain), Preston (hand)
#Team 4: Gabe (brain), Quinn (hand)
#Team 5: Sam (brain), Chaysen (hand)
#Team 6: Kevin (brain), Ethan M (hand)
#Team 7: Gage (brain), Eric (hand)


#You have until the Scenario is due to brainstorm an idea together, create a flowchart, and then
#turn that flowchart into functioning code. The code itself must have at least: 1 dictionary or list,
#1 loop, 2 if statements (elif and else statements tied to it does not count towards the total),
#1 variable with a user input, and 1 form of an assignment operator. You are free to add whatever else
#you feel is necessary to complete your concept. You will be graded based on how those ideas are
#implemented together.
from random import randint
from random import choice
print ("hello world")

from random import choice
from random import randint

#separates 100 into 2 halfs
half = randint (1,48)
half2 = 49 - half
#sets up the points
points = 0
#lives duh
lives = 3
while True:

    askchar = input("would you like to have custom characters? (y/n) ")
    if askchar == "y" or "yes":
        #ask for custom hellos and worlds

        customnames = []
        nameamount = int(input("How many custom names? "))
        for i in range (nameamount):
            name = input("name of next character you want ")
            customnames.append(name)
            print(customnames)
    elif askchar == "n" or "no":
        customnames.append("world")
        print(customnames)
    else:

        print(customnames)



    worlds = input("what do you want the hider to be named? say 0 for default ")
    if worlds == "0":
        worlds = "world"
        print(worlds)

    break


#a number that keeps track where the World is in the Hellos
total = 0
while True:
    half = randint (1,48)
    half2 = 49 - half
#for var half times it prints hello and keeps track what number it currently is on

    for i in range(half):
        total += 1
        print(choice(customnames), total)
#prints world and tottrue takes the number it is on
    total = total + 1
    print (worlds, total)
    tottrue = total
#finishes the hello chain until its 100
    for x in range(half2):
        total = total + 1
        print(choice(customnames), total)
#ask question and checks whether it is tottrue which is the same number world is on
    ans = int(input(f"what number is \"{worlds}\" at? :"))
    if ans == tottrue:
        print("you got it!")
        points = points + 1
        print("your score is", points)
        while True:
            #takes a break and asks you when you want to continue
            a = int(input("say 1 when you want to continue:"))
            if a == 1:
                total = 0
                break
    # if you get the question wrong your lives go down
    else:
        lives = lives - 1
        print("wRooOoNg")
        print("you have", lives, " lives")
        while True:
            a = int(input("say 1 when you want to continue:"))
            if a == 1:

                total = 0
                break
    #death check
    if lives == 0:
        print("you have", lives," lives. YOu lOOsE!")
        print("your score is", points)

        break