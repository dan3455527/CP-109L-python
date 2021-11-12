# question 2
# generate number between (1, 20), sum up until sum exceed 1000
# or generate more than 100 numbers

import random

sum_num = 0
generate_num_count = 0
while True:
    num = random.randint(1, 20)
    sum_num += num
    generate_num_count += 1
    if sum_num > 1000:
        print(sum_num)
        print("the sum exceeds 1000")
        break

    if generate_num_count > 100:
        print(sum_num)
        print("the number generate more than 100 times")
        break