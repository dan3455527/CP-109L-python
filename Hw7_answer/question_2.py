# turn for loop to while loop

x = int(input("input x value"))
i = 1
while i < x:
    if x % i == 0:
        print(i)
    i += 1
