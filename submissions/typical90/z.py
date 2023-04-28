from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

N = int(input())

tree = defaultdict(list)
for _ in range(N-1):
    A,B = map(int,input().split())
    tree[A-1].append(B-1)
    tree[B-1].append(A-1)


visited = [False]*N
color_0 = []
color_1 = []

def dfs(v, depth):
    visited[v] = True

    if depth%2 == 0:    color_0.append(v+1) 
    else:   color_1.append(v+1)

    for next_v in tree[v]:
        if visited[next_v]:    continue
        dfs(next_v, depth+1)

dfs(0,1)
# print(colors)

ans = color_1 if len(color_1) > len(color_0) else color_0
print(*ans[:N//2])

    
