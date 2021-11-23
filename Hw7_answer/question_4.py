# calculate and display the expression, no need to align

x = int(input("input the value: "))
sum_num = 0
for i in range(1, x+1):
    for j in range(1, i+1):
        print(j, end=" ")
        if j == i:
            print("=", end=" ")
        else:
            print("+", end=" ")
    sum_num += i
    print(sum_num)