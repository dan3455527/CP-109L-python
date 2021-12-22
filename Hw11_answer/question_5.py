

def CJK(ch):
    char_uni = ord(ch)
    if char_uni >= 0x2E80 and char_uni <= 0xFEFF:
        return True
    else:
        return False

string = input("input the string contained digit, chinese, alphabet:\n")
chinese_count = 0
for s in string:
    if CJK(s) == True:
        chinese_count += 1

