from collections import defaultdict

N, M = map(int, input().split())
UV = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    UV[u].append(v)

cnt = 0
for a in UV.keys():
    for b in UV[a]:
        if b in UV:
            for c in UV[b]:
                if c in UV[a] and a < b < c:   cnt += 1        

print(cnt)
