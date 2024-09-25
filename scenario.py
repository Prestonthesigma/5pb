#Preston Bidwell
#Scenario
#Fifth hour

villains = {
    "Thin White Duke":{
        "attack" : "throwing darts",
        "attack2": "malikuth",
        "Health" : 50,
        "Damage" : 34,
    },
    "King Crimson":{
        "attack" : "epitaph",
        "attack2": "starless",
        "Health" : 60,
        "Damage":  30,
    },
    "King Gizzard":{
        "attack" : "Shanghai",
        "attack2": "Field of Vision",
        "Health" : 80,
        "Damage" : 20,
    },
    "Lizard Wizard" :{
        "attack" : "PetroDragonic Apocalypse; or, Dawn of Eternal Night: An Annihilation of Planet Earth and the Beginning of Merciless Damnation",
        "attack2" : "Motor Spirit",
        "Health" : 1,
        "Damage" : 9999,
    },
    "Diamond Dog" :{
        "attack": "Fame",
        "attack2": "Pyschedelic Soul",
        "Health" : 30,
        "Damage" : 60,
    },

}

villains["Thin White Duke"]["Damage"] = int(input())
villains["King Crimson"]["Damage"] = int(input())
villains["King Gizzard"]["Damage"] = int(input())
villains["Lizard Wizard"]["Damage"] = int(input())
villains["Diamond Dog"]["Damage"] = int(input())

print(villains)

