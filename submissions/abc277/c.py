from collections import defaultdict,deque

N = int(input())
graph = defaultdict(list)
for _ in range(N):
    A,B = map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)

visited = defaultdict(int)
v = 1
Q = deque()
Q.append(v)
S = {1}
while Q:
    v = Q.popleft()
    visited[v] = 1
    for v2 in graph[v]:
        if not v2 in S:
            Q.append(v2)
            S.add(v2) 

print(max(S))
