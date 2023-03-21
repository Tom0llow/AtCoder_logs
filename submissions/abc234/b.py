import math 

N = int(input())
x, y = [0] * N, [0] * N

def dist_culc(x, y):
    dist = math.sqrt(x**2 + y**2)
    return dist 

for i in range(N):
    x[i], y[i] = map(int, input().split())

max_d = 0
for i in range(N):
    for j in range(i+1, N):
        d = dist_culc(x[i]-x[j], y[i]-y[j])
        if max_d < d:
            max_d = d
    
print(max_d)
