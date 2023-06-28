import math
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)


N,D = map(int,input().split())
people = [list(map(int,input().split())) for _ in range(N)]


def euclidean_distance(A,B):
    a1,a2 = A
    b1,b2 = B
    return math.sqrt((a1-b1)**2 + (a2-b2)**2)


G = defaultdict(list)
for i in range(N-1):
    for j in range(i+1,N):
        if euclidean_distance(people[i], people[j]) <= D:
            G[i].append(j)
            G[j].append(i)

# print(G)
virus = [False]*N
def dfs(v):
    virus[v] = True
    for nv in G[v]:
        if virus[nv]:   continue
        dfs(nv)

dfs(0)
# print(virus)
for flag in virus:
    ans = 'Yes' if flag else 'No'
    print(ans)
