from collections import deque

N,X,Y = map(int,input().split())
X -= 1
Y -= 1

T = [[] for _ in range(N)]
path = [-1 for _ in range(N)]    

for i in range(N-1):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    T[u].append(v)
    T[v].append(u)

Q = deque([(X,0)])
while Q:
    x,cost = Q.popleft()
    if path[x] != -1:
        continue

    path[x] = cost
    for nx in T[x]:
        Q.append((nx,cost+1))

ans = []
v = Y
while path[v] != 0:
    ans.append(v+1)
    for px in T[v]:
        if path[px] == path[v]-1:
            v = px
            break

ans.append(X+1)
print(' '.join(map(str,ans[::-1])))
