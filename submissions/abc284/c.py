from collections import defaultdict
N,M = map(int,input().split())

graph = defaultdict(list)
for _ in range(M):
    u,v = map(int,input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

visited = [False for _ in range(N)]
def dfs(graph,v):
    visited[v] = True
    for e in graph[v]:
        if not visited[e]:
            dfs(graph,e)

cnt = 0
for i in range(N):
    if not visited[i]:
        dfs(graph,i)
        cnt += 1

print(cnt)
