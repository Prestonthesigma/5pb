#Preston
#5th Hour
#HW18


#1. Import the "random" library and create a def function that prints "Hello World!"
import random

def helloworld():
    print("Hello World!")
helloworld()
#2. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanBag = ["yellow bean", "red bean", "orange bean", "purple bean","green bean"]
#3. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def randombean():
    if not beanBag:
        print("List is empty")
    else:
        bean = random.choice(beanBag)
        print(bean)
        beanBag.remove(bean)
        repeatgame()
#4. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def repeatgame():
    replayInput = input("Would you like to play again? Y/N ")
    if replayInput == "Y" or replayInput == "y":
       randombean()
    else:
        exit()
#5. Call the #3 function at the bottom.
randombean()

