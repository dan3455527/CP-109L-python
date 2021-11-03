# question 4
# metric conversion


distance = float(input("enter the distance travelled (in km): "))
volume = float(input("volume of tank (in liter): "))

fuel_mileage_rate = volume / (100 * distance)
fuel_efficiency = distance / volume
mpg = (distance * 0.621) / (volume * 0.264) # 1 km = 0.621 mile, 1 liter = 0.264 gallon

print("fuel mileage rate =  ", fuel_mileage_rate)
print("fuel efficiecy    =  ", fuel_efficiency)
print("mpg               =  ", mpg)
