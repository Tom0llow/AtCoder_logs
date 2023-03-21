import itertools as it
import numpy as np

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

num = list(range(1, N+1))
per_num = list(it.permutations(num))

for i in range(len(per_num)):
    if P == per_num[i]: a = i + 1
    if Q == per_num[i]: b = i + 1

ans = np.abs(a - b)
print(ans)
