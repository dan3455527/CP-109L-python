# question 4
# add line_number

import random

line_number = 1
while True:
    computer_draw = random.randint(1, 10)
    print(f"{line_number:2d}) the computer draws {computer_draw}")
    line_number += 1
    if computer_draw == 7:
        print("The end.")
        break