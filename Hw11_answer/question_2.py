# print table of cosin 0 -120 degree step of 0.1

import math
degree = 0.0
print(f"{'theta':<5}{'cos':>15}\n")
while degree <= 120.0:
    rad = degree * math.pi / 180
    cosine = math.cos(rad)
    print(f"{degree:^5.1f}{cosine:>15.6f}\n")
    degree += 0.1
    
