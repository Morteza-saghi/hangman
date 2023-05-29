from words import words
from random import randint as rand
randomNum = rand(0, len(words) - 1)
chosenWord = words[randomNum]
# print(chosenWord)

temp = str()

for i in chosenWord:
    temp += "-"

healthBar = 10
chosedLetters = list()

chosenWord = list(chosenWord)
temp3 = str()

# use this function to validate the input and status of the game


def complition():
    temp2 = str()
    global temp3
    for i in chosenWord:
        if i in chosedLetters:
            temp2 += i
        else:
            temp2 += "-"
    print(temp2)
    temp3 = temp2

# use this function to see if the game is done or not


def gameFinished():
    theFinish = bool()
    for i in temp3:
        if i == "-":
            theFinish = False
        else:
            theFinish = True
    return theFinish


# we stay in this loop to keep playing the game
while healthBar > 0:
    if gameFinished() == True:
        print("You Have Won Bitch")
        break
    theinput = input("please enter your guess\n")
    if theinput in chosenWord:
        print("guesed right motherfucker\n")
        chosedLetters.append(theinput)
        print(f"You Still Have {healthBar} Hearts")
        complition()
        print(f"You Have Chosed Theese Letters {chosedLetters}")
        print("====================")
    else:
        print("Not There...\nYou Better Work Bitch")
        healthBar -= 1
        chosedLetters.append(theinput)
        print(f"You Still Have {healthBar} Hearts")
        complition()
        print(f"You Have Chosed Theese Letters {chosedLetters}")
        print("====================")
# new shit
