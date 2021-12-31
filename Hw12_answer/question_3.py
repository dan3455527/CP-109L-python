def CJK(ch):
    char_uni = ord(ch)
    if char_uni >= 0x2E80 and char_uni <= 0xFEFF or char_uni >= 0x20000:
        return True
    else:
        return False

def isCJKsymbol(ch):
    char_uni = ord(ch)
    if (char_uni >= 0x3000 and char_uni <= 0x303F) or (char_uni >= 0xFF00 and char_uni <= 0xFFEF):
        return True
    else:
        return False

def isAlpha(ch):
    char_uni = ord(ch)
    if (char_uni >= 0x0041 and char_uni <= 0x005A) or (char_uni >= 0x0061 and char_uni <= 0x007A):
        return True
    else:
        return False

def isDigit(ch):
    char_uni = ord(ch)
    if char_uni >= 0x0030 and char_uni <= 0x0039:
        return True
    else:
        return False

def isEngSymbol(ch):
    char_uni = ord(ch)
    if ((char_uni >= 0x0020 and char_uni <= 0x002F) or (char_uni >= 0x003A and char_uni <= 0x0040) or 
            (char_uni >= 0x005B and char_uni <= 0x0060) or (char_uni >= 0x007B and char_uni <= 0x007E)):
        return True
    else:
        return False
#TODO
# output statistic:
# english alphabet/ digit/ English symbol/ chinese/ chinese symbol
file = open("./Hw12_answer/e_paper_big5.txt", "r", encoding="cp950")
words = file.read()

count_eng_alphabet = 0
count_digit = 0
count_eng_symbol = 0
count_ch_char = 0
count_ch_symbol = 0

for word in words:
    if CJK(word):
        count_ch_char += 1
    elif isCJKsymbol(word):
        count_ch_symbol += 1
    elif isAlpha(word):
        count_eng_alphabet += 1
    elif isDigit(word):
        count_digit += 1
    elif isEngSymbol(word):
        count_eng_symbol += 1
    else:
        pass

print(f"eng_alpha_count : {count_eng_alphabet}")
print(f"digit count : {count_digit}")
print(f"english symbol count : {count_eng_symbol}")
print(f"chinese char count : {count_ch_char}")
print(f"chinese symbol count : {count_ch_char}")

#OUTPUT
# eng_alpha_count : 176
# digit count : 24
# english symbol count : 181
# chinese char count : 2907
# chinese symbol count : 2907