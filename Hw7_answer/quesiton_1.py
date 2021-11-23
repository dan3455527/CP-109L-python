# find leap year

for year in range(1900, 2020):
    # check leap year
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        print(f"year {year} is leap year")
