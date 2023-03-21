from collections import defaultdict

d_x, d_y = defaultdict(int), defaultdict(int)
for _ in range(3):
    x, y = map(int, input().split())
    d_x[x] += 1
    d_y[y] += 1

for key, value in d_x.items():
    if value == 1: ans_x = key
for key, value in d_y.items():
    if value == 1: ans_y = key

print(ans_x, ans_y)
 
