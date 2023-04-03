from collections import defaultdict, deque


N,M = map(int,input().split())
G = defaultdict(list)
indegree = defaultdict(int)
for _ in range(M):
    u,v = map(int,input().split())
    G[u-1].append(v-1)
    indegree[v-1] += 1


def topological_sort(G, indegree, V):
    sorted_vertices = []
    
    que = deque()
    for i in range(V):
        if indegree[i] == 0:
            que.append(i)

    while que:
        v = que.popleft()

        for i in range(len(G[v])):
            u = G[v][i]
            indegree[u] -= 1
            if indegree[u] == 0:    que.append(u)

        sorted_vertices.append(v)

    return sorted_vertices


sorted_vertices = topological_sort(G, indegree, N)
# print(sorted_vertices)


import sys
sys.setrecursionlimit(10**6)


visited = [False]*N
dp = [0]*N

def dfs(v):
    if visited[v]: return dp[v]
    
    visited[v] = True
    for u in G[v]:
        res = dfs(u)
        dp[v] = max(dp[v], res+1)

    return dp[v]

ans = 0
for i in range(N):
    ans = max(ans, dfs(i))
print(ans)
