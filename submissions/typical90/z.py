from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

N = int(input())

G = defaultdict(list)
for _ in range(N-1):  
    A,B = map(int,input().split())
    G[A-1].append(B-1)
    G[B-1].append(A-1)


color = [-1]*N
def dfs(G,v):
    for v2 in G[v]:
        if color[v2] != -1: continue
        color[v2] = 1-color[v]
        dfs(G,v2)
        

for v in range(N):
    if color[v] != -1:  continue
    color[v] = 1
    dfs(G,v)

# print(color)
white_v = [v+1 for v in range(N) if color[v] == 1]
black_v = [v+1 for v in range(N) if color[v] == 0]

ans = black_v if len(white_v) < len(black_v) else white_v
print(*ans[:N//2])
