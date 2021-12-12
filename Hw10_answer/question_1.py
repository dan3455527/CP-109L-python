# capitalize all letter

input_str = input("input a string")

alternate_str = ""
for i in range(len(input_str)):
    if i % 2 == 0 :
        alternate_str = alternate_str + input_str[i]
    else:
        alternate_str = alternate_str + input_str[i].upper()
print(alternate_str)
