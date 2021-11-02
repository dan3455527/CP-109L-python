# question 3

def formula_calculation():
    x = float(input("enter value of x: "))
    answer = (x ** 4 + 7 * x ** 3 - 3 * x ** 2)/5
    print(f"calculate result = {answer}")
    return None


if __name__ == "__main__":
    formula_calculation() # try input 2
    formula_calculation() # try input -2.5
