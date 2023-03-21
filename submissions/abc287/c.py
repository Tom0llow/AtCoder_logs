import sys
sys.setrecursionlimit(10**6)

N,M = map(int,input().split())
G = [tuple(map(int,input().split())) for _ in range(M)]

P = [-1]*N

def root(x):
    if P[x] < 0:
        return x
    P[x] = root(P[x])
    return P[x]

def unite(x,y):
    x = root(x)
    y = root(y)
    if x == y:
        return
    P[x] += P[y]
    P[y] = x

degree = [0]*N

for i in range(M):
    a,b = G[i]
    a -= 1
    b -= 1
    degree[a] += 1
    degree[b] += 1

    if root(a) == root(b):
        print('No')
        exit()

    unite(a,b)

if M == N-1 and max(degree) <= 2:
    print('Yes')
else:
    print('No')
