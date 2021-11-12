# question 4
# advanced rock paper scissor game

import random

user_win_count = 0
tie_count = 0
user_lose_count = 0

while True:
    user_hand = int(input("enter your hand (0=rock, 1=paper, 2=scissors): "))
    computer_hand = random.randint(0, 2)
    if user_hand == -1:
        print("statistic: ")
        print("user wins: ", user_win_count, "games")
        print("user lose: ", user_lose_count, "games")
        print("game ties: ", tie_count, "games")
        print("wining rate", user_win_count, "wins out of ", user_win_count+tie_count+user_lose_count)
        break

    if (computer_hand == 0):
        print("computer hand is : rock")
        if (user_hand == 0):
            print("user hand is : rock")
            print("game is tie")
            tie_count += 1
        elif (user_hand == 1):
            print("user hand is : paper")
            print("user's win")
            user_win_count += 1
        elif (user_hand == 2):
            print("user hand is : scissor")
            print("computer's win")
            user_lose_count += 1

    elif (computer_hand == 1):
        print("computer hand is : paper")
        if (user_hand == 0):
            print("user hand is : rock")
            print("computer's win")
            user_lose_count += 1
        elif (user_hand == 1):
            print("user hand is : paper")
            print("the game is tie")
            tie_count += 1
        elif (user_hand == 2):
            print("user hand is : scissor")
            print("user's win")
            user_win_count += 1

    elif (computer_hand == 2):
        print("computer hand is : scissors")
        if (user_hand == 0):
            print("user hand is : rock")
            print("user's win")
            user_win_count += 1
        elif (user_hand == 1):
            print("user hand is : paper")
            print("computer's win")
            user_lose_count += 1
        elif (user_hand == 2):
            print("user hand is : scissor")
            print("the game is tie")
            tie_count += 1



