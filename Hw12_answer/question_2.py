import math

file = open("./Hw12_answer/sin.txt", "r")
new_file = open("./Hw12_answer/sin_cos.txt", "w")

lines = file.readlines()
head_format = "{:^10s}{:^10s}{:^10s}{:^10s}\n"
table_format = "{:>10.6f}{:>10.6f}{:>10.6f}{:>10.6f}\n"

for i in range(0, len(lines)):
    words = lines[i].split()
    if i == 0:
        new_line = head_format.format(words[0], words[1], "cos", "sin+cos")
        new_file.write(str(new_line))
    else:
        angle = float(words[0])
        sin_value = float(words[1])
        cos_value = math.cos(angle*math.pi/180)
        sin_cos_value = sin_value + cos_value
        new_line = table_format.format(angle, sin_value, cos_value, sin_cos_value)
        new_file.write(str(new_line))

new_file.close()