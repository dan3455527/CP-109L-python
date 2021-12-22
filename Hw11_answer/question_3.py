

def isLeap(y):
    if (y % 4 == 0) and (y % 100 != 0 or y % 400 == 0):
        result = True
    else:
        result = False
    
    return result


for y in range(1900, 2021):
    print(f"{y:<5}{isLeap(y)}")
