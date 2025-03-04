#Name:
#Class: 5th Hour
#Assignment: HW21
from operator import truediv

#1. Make a nested dictionary with three entries called "sport1", "sport2", and "sport3" containing
#the name a sport the school partakes in, the amount of players a typical team uses during gameplay
#(ex: Basketball has 5 players), and if the sport uses a ball or not (as a boolean).
sport1 = {
    "Football": 11,
    "ball": True
},

sport2 = {
    "soccer": 19,
    "ball": True

},

sport3 = {
    "Basketball": 5,
    "ball": True
}
#2. Create a def function that pulls the values from the dictionary as arguments, adds together the
#players of all three sports, and prints the sum
def sport_sum(a,b,c):
    SportSum= a + b + c
    print(SportSum)
#3. Call the function with arguments here
sport_sum(11,19,5)