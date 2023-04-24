from collections import defaultdict, deque
import sys

sys.setrecursionlimit(10**6)

N = int(input())
G = defaultdict(list)
for _ in range(N-1):
    A,B = map(int,input().split())
    G[A-1].append(B-1)
    G[B-1].append(A-1)

# print(G)

d = [0]*N
def dfs_for_length(s,v):
    for nv in G[v]:
        if d[nv] != 0 or nv == s:  continue
        
        d[nv] = d[v]+1
        dfs_for_length(s,nv)

dfs_for_length(0,0)
i = d.index(max(d))

d = [0]*N
dfs_for_length(i,i)
ans = max(d)+1
print(ans)
