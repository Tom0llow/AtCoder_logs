from collections import defaultdict
import bisect


N,M = map(int,input().split())

G = defaultdict(list)
for _ in range(M):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)


ans = 0
for k,l in G.items():
    if bisect.bisect_right(sorted(l),k) == 1:
        ans += 1

print(ans)
