# question 5
# mark * and lucky if number match
import random

line_number = 1
while True:
    computer_draw = random.randint(1, 10)
    if line_number == computer_draw:
        print(line_number, ") * the computer draws", computer_draw, "(lucky)")
    else:
        print(line_number, ") the computer draws ", computer_draw)
    line_number += 1
    if computer_draw == 7:
        print("The end.")
        break