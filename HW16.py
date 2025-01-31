#Preston
#5th Hour
#HW16

#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".

#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.

import random

def rockpaperscissors():
   userinput = int(input("1 for rock, 2 for paper, or 3 for scissors"))
   otherplay = random.randint (1, 3)
   if userinput == 1 and otherplay == 3:
       print("you win")
   elif userinput == 1 and otherplay == 2:
       print('you lose')
   elif userinput == 1 and otherplay == 1:
       print("draw")

   elif userinput == 2 and otherplay == 1:
       print("you win")
   elif userinput == 2 and otherplay == 3:
       print('you lose')
   elif userinput == 2 and otherplay == 2:
       print("draw")

   elif userinput == 3 and otherplay == 2:
       print("you win")
   elif userinput == 3 and otherplay == 1:
       print('you lose')
   elif userinput == 3 and otherplay == 3:

       print("draw")
   repeatgame()



def repeatgame():
    replayInput = input("Would you like to play again? Y/N ")

    # Note here how you can call the function inside of itself to repeat the code.
    if replayInput == "Y" or replayInput == "y":
        rockpaperscissors()
    else:
        exit()




rockpaperscissors()
