# compare and upper the long one, cap the second one

str_1 = input("input the first word : ")
str_2 = input("input the second one : ")

if len(str_1) > len(str_2):
    str_1 = str_1.upper()
    str_2 = str_2.capitalize()

else:
    str_2 = str_2.upper()
    str_1 = str_1.capitalize()

print(str_1)
print(str_2)