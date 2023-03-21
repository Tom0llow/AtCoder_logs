from collections import defaultdict

N,M = map(int,input().split())
G = defaultdict(list)
for _ in range(M):
    u,v = map(int,input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)

visited = [0]*N

for i in range(N):
    if visited[i]:
        continue

    q = [i]
    size = 0
    visited[i] = 1
    count = 0
    while q:
        now = q.pop()
        size += 1
        count += len(G[now])
        for next in G[now]:
            if visited[next]:
                continue
            visited[next] = 1
            q.append(next)

    if size*2 != count:
        print('No')
        exit()

print('Yes')
