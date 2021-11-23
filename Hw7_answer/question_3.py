# calculate \sum{k=1}^X \frac{1}{k}

x = int(input("input the x value: "))
result = 0
for k in range(1, x+1):
    result = result + (1/k)

print(f"the sum result is {result}")
