import itertools
import math

N = int(input())
point = [list(map(int, input().split())) for _ in range(N)]

num = list(range(N))
ptn = list(itertools.permutations(num))

sum_dist = 0

for p in ptn:
    for i in range(len(p)-1):
        a, b = p[i], p[i+1]
        x1, y1 = point[a][0], point[a][1]
        x2, y2 = point[b][0], point[b][1]
        sum_dist += math.sqrt((x2-x1)**2 + (y2-y1)**2)

ans = sum_dist / len(ptn)
print(ans)
