from collections import defaultdict


N,M = map(int,input().split())

d = defaultdict(list)
for _ in range(M):
    A,B = map(int,input().split())
    d[A].append(B)
    d[B].append(A)

for n in range(1,N+1):
    print(len(d[n]),*sorted(d[n]))
