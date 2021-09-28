# week one exercise, algorithm
import math

class Exercise:
    def get_common_divider(int1, int2):
        int_list = sorted((int1, int2))
        while True:
            R = int_list[1] % int_list[0]
            if R != 0:
                int_list[1] = int_list[0]
                int_list[0] = R
            else:
                break
        return int_list[0] # common divider
            

if __name__ == "__main__":
    print(Exercise.get_common_divider())