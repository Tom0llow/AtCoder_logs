from collections import defaultdict,deque

N = int(input())
graph = defaultdict(list)
for _ in range(N-1) :
	a,b = map(int, input().split())
	graph[a-1].append(b-1)
	graph[b-1].append(a-1)
 
def dfs(s):
    dist = [-1]*N
    dist[s] = 0
    
    Q = deque()
    Q.append(s)
    while Q:
        v = Q.popleft()
        for nv in graph[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v]+1
                Q.append(nv)
    return dist
 
# –Ø‚Ì’¼Œa‚ğ‹‚ß‚é‚É‚ÍAÅ’Z‹——£ŒvZ‚ğ2‰ñs‚¤D
dist0 = dfs(0)
endPoint = max(dist0)
dist0 = dfs(dist0.index(endPoint))
 
print(max(dist0)+1)
