


# 2 digit
for num in range(1, 100):
    digit_1 = num // 10
    digit_0 = num % 10
    sum_digit = digit_0 + digit_1
    # print(f"{num}sum digit:{sum_digit}")
    if num % sum_digit == 0:
        print(f"{num}:{sum_digit} <-- is a divisor")
# 3 digit
for num in range(100, 351):
    digit_0 = num % 10
    digit_1 = num // 10
    digit_2 = digit_1 // 10
    digit_1 = digit_1 % 10
    sum_digit = digit_0 + digit_1 + digit_2
    # print(f"{num}sum digit:{sum_digit}")
    if num % sum_digit == 0:
        print(f"{num}:{sum_digit} <-- is a divisor")

