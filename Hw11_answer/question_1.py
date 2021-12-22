# count digit, letter, special character

digit_ls = "1234567890"
letter_ls = "abcdefghijklmnopqrstuvwxyz"

digit_count = 0
letter_count = 0
special_char_count = 0

input_str = input("enter the string :")
for str in input_str:
    if str in digit_ls:
        digit_count += 1
    elif str.lower() in letter_ls:
        letter_count += 1
    else:
        if not str == " ":
            special_char_count += 1
        else:
            pass
print(f"{'digit':<10}{digit_count:>3}\n"
      f"{'letters':<10}{letter_count:>3}\n"
      f"{'specials':<10}{special_char_count:>3}")

