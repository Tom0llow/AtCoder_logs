from collections import defaultdict,deque
 
N,M = map(int,input().split())
 
G = defaultdict(list)
deg = [0 for _ in range(N)]
for _ in range(M):
    A,B,C,D = input().split()
    a,c = int(A)-1,int(C)-1
    G[a].append(c)
    G[c].append(a)
    deg[a] += 1
    deg[c] += 1
 
x,y = 0,0
visited = [False for _ in range(N)]
for i in range(N):
    if not visited[i]:
        Q = deque([])
        visited[i] = True
        Q.appendleft(i)
        f = True
        while Q:
            q = Q.popleft()
            if deg[q] != 2: f = False
            for v in G[q]:
                if not visited[v]:
                    Q.appendleft(v)
                    visited[v] = True
 
        if f:   x += 1
        else:   y += 1
 
print(x,y)
