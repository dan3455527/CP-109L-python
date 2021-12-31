file = open("./Hw12_answer/sin.txt", "r")
new_file = open("sin_v2.txt", "w")
lines = file.readlines()
head_format = "{:^10s}{:^10s}"
table_format = "{:<10.6f}{:<10.6f}"

for i in range(0, len(lines), 3):
    words = lines[i].split()
    if i == 0:
        new_line = head_format.format(words[0], words[1])
        new_file.write(new_line)
    else:
        new_line = table_format.format(float(words[0]), float(words[1]))
        new_file.write(new_line)
    # new_file.write(lines[i])

new_file.close()
