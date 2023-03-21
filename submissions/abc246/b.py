import numpy as np

A, B = map(int, input().split())

def calc_dist(A, B):
    dist = np.sqrt(A**2 + B**2)
    return dist

dist = calc_dist(A, B)
ans_x, ans_y = A*(1/dist), B*(1/dist)
print(ans_x, ans_y)
