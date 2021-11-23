# get sqrt until root less than 2

num = int(input("input a number greater than 2: "))
counter = 1
while True:
    if num < 2:
        break
    print(f"{counter} : {num**0.5}")
    num = num ** 0.5
    counter += 1
