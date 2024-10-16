#Name: Preston
#Class: 5th Hour
#Assignment: Scenario 3
import random

#Step 1: Copy enemy dictionary from SC1

#Step 2: Copy party dictionary from SC2

#Step 3: Make sure every enemy and party member has health points (fixed)

#Step 4: Make sure every enemy and party member has an attack modifier (fixed)

#Step 5: Make sure every enemy and party member has an armor class (AC) (fixed)

#Step 6: Make every enemy and party member has a damage roll (random)


#Once both dictionaries are updated, create a combat
#prototype that has a party member attack first, then an enemy
#attacks back right after.

#To determine if a creature hits another creature, you roll a
#20-sided die (d20) and add the attack modifier to the roll.
#If that number is the same as or higher than the enemy's Armor Class
#(AC), the attack hits, and you roll for damage. If it is lower, the
#attack misses. If an enemy or party member hits zero (0) health
#points, they die.

#Step 7: Pick a party member

#Step 8: Pick an enemy

#Step 9: Create an attack roll for party member

#Step 10: Compare the party member attack roll to the enemy AC

#Step 11: Subtract damage from enemy health if it hits

#Step 12: Check to see if enemy is still alive

#Step 13: Step 9 through 12, but enemy attacks party member if still alive




#Party Dictionary Goes Here
party = {
    "Thin White Duke":{
        "attack" : "throwing darts",
        "Health" : 18,
        "AC": 12,
        "damage":random.randint (1,4),
        "hitroll": random.randint (1,20),
    },
    "King Crimson":{
        "attack": "starless",
        "Health" : 20,
        "AC" : 13,
    },
    "King Gizzard":{
        "attack" : "Shanghai",
        "Health" : 25,
        "AC" : 13,

    },
    "Lizard Wizard" :{
        "attack" : "PetroDragonic Apocalypse; or, Dawn of Eternal Night: An Annihilation of Planet Earth and the Beginning of Merciless Damnation",
        "Health" : 1,
        "AC" : 17,
    },
    "Diamond Dog" :{
        "attack": "Fame",
        "Health" : 30,
        "AC" : 13,
        "Damage": random.randint (1,5)
    },

}



#Enemy Dictionary Goes Here
enemyDict = {
    "LaeZel" : {
        "Race" : "Githyanki",
        "Class" : "Fighter",
        "Background" : "Soldier",
        "Health" :  12,
        "AC" : 17,
       "Damage": random.randint (1,6)+random.randint(1,6) + 3
    },
    "Shadowheart" : {
        "Race" : "Half-Elf",
        "Class" : "Cleric",
        "Background" : "Acolyte",
        "Health" : 10,
        "AC" : 14,
        "Damage": random.randint(5,8),
        "hitroll":random.randint(1,20)

    },
    "Gale" : {
        "Race" : "Human",
        "Class" : "Wizard",
        "Background" : "Sage",
        "Health" : 8,
        "AC" : 14,
        "Damage": random.randint(1, 10)
    },
    "Astarion" : {
        "Race" : "High Elf",
        "Class" : "Rogue",
        "Background" : "Charlatan",
        "Health" : 10,
        "AC" : 14,
        "Damage": random.randint(5,10)
    }
}


#Combat Code Goes Here
if (party["Thin White Duke"]["hitroll"]) >= (enemyDict["Shadowheart"]["AC"]):
    (enemyDict["Shadowheart"]["Health"]) - (party["Thin White Duke"]["damage"])
    print("Thin White Duke's Attack hit.")
    if (enemyDict["Shadowheart"]["Health"]) <=0:
        print("Shadowheart is dead")
        exit()
    else:
        print("Shadowheart's attack missed")

if (enemyDict["Shadowheart"]["hitroll"]) >= (party["Thin White Duke"]["AC"]):
    (party["Thin White Duke"]["Health"]) - (enemyDict["Shadowheart"]["Damage"])
    print("Shadowheart's attack hit.")
    if (enemyDict["Shadowheart"]["Health"]) <= 0:
        print("Thin White Duke is dead")
    else:
        print("Thin White Duke's attack missed")


