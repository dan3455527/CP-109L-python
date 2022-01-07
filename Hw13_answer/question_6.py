input_str = input("input a string : ")
sort_char_list = []
for char in input_str:
    sort_char_list.append(char)
sort_char_list.sort()
result = ""
for sort_char in sort_char_list:
    result = result + sort_char
print(f"result: {result}")