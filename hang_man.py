import random
import time

Fruits = ['pea','mango','quava','pineapple','apple','grapes','orange','melon']
Superheroes =['iron man','captain america','thor','antman','statham']

userGuessList = []
userGuesses = []
playGame = True
category = ""
continueGame = "Y"

#welcoming the user
name = input("Enter your name")
print("helloo," + name.capitalize(),"Time to play hangman")
print("")
#wait for 2 second
time.sleep(2)
print(">>>>The objective of the game is to guess the secret word chosen by the computer.")
time.sleep(2)
print(">>>You can guess only one letter at a time. Dont forget to press 'Enter key' after each guess")
time.sleep(2)
print(">>>Have fun......")
time.sleep(0.5)

#choosing the secret word

while True:
    if category.upper() == 'S':
        secretWord = random.choice(Superheroes)
        break
    elif category.upper() =='F':
        secretWord = random.choice(Fruits)
        break
    else:
        category = input("please select a valid category: F for Fruits / S for Super-Heroes; X to exit")
        if category.upper() == 'X':
            print("bye. see u next time!!")
            playGame = False
            break
if playGame:
    secretWordList = list(secretWord)
    attempts = (len(secretWord) + 2)

    userGuessList = []
    






