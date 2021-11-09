# question 4
# rock paper scissor game

import random



user_hand = int(input("enter your hand (0=rock, 1=paper, 2=scissors): "))
computer_hand = random.randint(0, 2)

if (computer_hand == 0):
    print("computer hand is : rock")
    if (user_hand == 0):
        print("user hand is : rock")
        print("game is tie")
    elif (user_hand == 1):
        print("user hand is : paper")
        print("user's win")
    elif (user_hand == 2):
        print("user hand is : scissor")
        print("computer's win")

elif (computer_hand == 1):
    print("computer hand is : paper")
    if (user_hand == 0):
        print("user hand is : rock")
        print("computer's win")
    elif (user_hand == 1):
        print("user hand is : paper")
        print("the game is tie")
    elif (user_hand == 2):
        print("user hand is : scissor")
        print("user's win")

elif (computer_hand == 2):
    print("computer hand is : scissors")
    if (user_hand == 0):
        print("user hand is : rock")
        print("user's win")
    elif (user_hand == 1):
        print("user hand is : paper")
        print("computer's win")
    elif (user_hand == 2):
        print("user hand is : scissor")
        print("the game is tie")

