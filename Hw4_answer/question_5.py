# question 4


def metric_conversion():
    distance = float(input("enter the distance travelled (in km): "))
    volume = float(input("volume of tank (in liter): "))

    fuel_mileage_rate = volume / (100 * distance)
    fuel_efficiency = distance / volume
    mpg = (distance * 0.621) / (volume * 0.264) # 1 km = 0.621 mile, 1 liter = 0.264 gallon

    print(f"result:\nfuel mileage rate = {fuel_mileage_rate:.3f}\n"\
          f"fuel efficiecy    = {fuel_efficiency:.3f}\n"\
          f"mpg               = {mpg:.3f}")
    return None


if __name__ == "__main__":
    metric_conversion()
