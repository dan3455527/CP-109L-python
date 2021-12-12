
upside_down_low = "ɐqᴐpǝɟƃɥı!ʞlɯuodbɹsʇnʌmxʎz"
upside_down_up = "∀ᗺↃᗡƎℲ⅁HIɾʞ⅂WNOdÒᴚS⊥∩ΛMX⅄Z"

normal_low = "abcdefghijklmnopqrstuvwxyz"
normal_up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

input_str = input("input the sentence:\n")

convert_str = ""
for i in input_str[::-1]:
    if i in normal_low:
        convert_str = convert_str + upside_down_low[normal_low.index(i)]
    elif i in normal_up:
        convert_str = convert_str + upside_down_up[normal_up.index(i)]
    else:
        convert_str = convert_str + i
print(convert_str)
