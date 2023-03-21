from collections import defaultdict

N,M = map(int,input().split())

d = defaultdict(set)
for _ in range(M):
    kx = list(map(int,input().split()))
    for x in kx[1:]:
        for y in kx[1:]:
            d[x].add(y)

ans = 'Yes'
for v in d.values():
    if len(v) != N:
        ans = 'No'
        break
  
print(ans) 
