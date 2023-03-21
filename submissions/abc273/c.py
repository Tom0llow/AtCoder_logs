import bisect
from collections import defaultdict

N = int(input())
A = list(map(int,input().split()))

B = sorted(set(A))
l = []
for a in A:
    n = len(B)-bisect.bisect_right(B,a)
    l.append(n)

l = sorted(l)
d = defaultdict(int)
for v in l:
    d[v] += 1

for k in range(N):
    print(d[k])        


    
