# check prime number

import math
n = int(input("input the number n: "))
is_prime = True
for i in range(2, n):
    if n % i == 0:
        is_prime = False
    if i > math.sqrt(n):
        break
print(f"is {n} prime number: {is_prime}")