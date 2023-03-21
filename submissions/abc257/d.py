from collections import deque

N = int(input())
x, y, P = [None]*N, [None]*N, [None]*N
for i in range(N):  
    x[i], y[i], P[i] = map(int, input().split())

costs = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        d = abs(x[i]-x[j]) + abs(y[i]-y[j])
        costs[i][j] = (d+P[i]-1) // P[i]
        costs[j][i] = (d+P[j]-1) // P[j]

def is_ok(s):
    for i in range(N):
        used = set([i])
        Q = deque({i})
        while Q:
            u = Q.popleft()
            for v in range(N):
                if (v not in used) and (s >= costs[u][v]):
                    used.add(v) 
                    Q.append(v)
        if len(used) == N:
            return True
    return False    

ng = 0
ok = 4*10**9
while abs(ok-ng) > 1:
    m = (ok+ng) // 2
    if is_ok(m):    ok = m
    else:   ng = m

print(ok)
