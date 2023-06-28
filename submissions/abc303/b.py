from collections import defaultdict


N,M = map(int,input().split())
d = defaultdict(set)
for _ in range(M):
    a = list(map(int,input().split()))
    
    for i in range(N-1):
        d[a[i]].add(a[i+1])
        d[a[i+1]].add(a[i])

# print(d)
s = set()
for k,v in d.items():    
    l = list(range(1,N+1))
    l.remove(k)

    for p in v:
        if p in l:
            l.remove(p)

    for p in l:
        s.add(tuple(sorted([k,p]))) 

print(len(s))
