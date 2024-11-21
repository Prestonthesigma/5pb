#Preston
#5th Hour
#Scenario 4

#Scenario 4:
#Due to scope creep leading to high development costs, the RPG you were working on has been
#shelved for the time being. You have been transferred to a new team working on a mobile game
#that allows you to dress up a model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.


print ("Hello World")

player = int(input("Number of Players:"))
print(player)

sum = 0

i = 0
while i < player:
    rating = int(input("Rate from 1-5"))
    if rating > 5 or rating < 1:
        print("error")
    else:
        i += 1
        sum += rating


average = sum/player

print(average)