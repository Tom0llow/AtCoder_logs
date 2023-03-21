import sys
sys.setrecursionlimit(10 ** 6)

N,M = map(int,input().split())
G = [tuple(map(int, input().split())) for _ in range(M)]

p = [-1]*N

def root(x):
    if p[x] < 0:
        return x
    p[x] = root(p[x])
    return p[x]

def unite(x,y):
    x = root(x)
    y = root(y)
    if x == y:
        return
    p[x] += p[y]
    p[y] = x


cnt = 0
for i in range(M):
    a,b = G[i]
    a,b = a-1,b-1
    
    if root(a) == root(b):
        cnt += 1
    
    unite(a,b)

print(cnt)
