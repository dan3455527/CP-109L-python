# question 3
# draw random int until print 7
import random

while True:
    computer_draw = random.randint(1, 10)
    print(f"the computer draws {computer_draw}")
    if computer_draw == 7:
        print("The end.")
        break