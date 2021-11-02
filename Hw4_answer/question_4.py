# question 4

def bmi_calculation():
    weight = float(input("input the weight(kg): "))
    height = float(input("input the height(meter): "))
    bmi = weight/(height ** 2)
    print(f"your BMI is : {bmi:.2f} kg/m^2")
    return None

if __name__ == "__main__":
    bmi_calculation()

