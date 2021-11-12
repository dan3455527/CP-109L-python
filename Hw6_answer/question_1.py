# question 1
# prompt user for number
# print abs value if not positive
# prompt for another num if not positive

while True:
    num = int(input('enter a number : '))
    if num < 0:
        num = num * -1
        print("the absolute value of the number is : ", num)
    elif num >= 0:
        break
    

