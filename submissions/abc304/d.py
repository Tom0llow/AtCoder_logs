from bisect import bisect_left
from collections import defaultdict


W,H = map(int,input().split())
N  = int(input())
pq = [list(map(int,input().split())) for _ in range(N)]
A = int(input())
a = list(map(int,input().split()))
B = int(input())
b = list(map(int,input().split()))


Counter = defaultdict(int)
for p,q in pq:
    i = bisect_left(a,p)
    j = bisect_left(b,q)
    Counter[(i,j)] += 1

# print(Counter)
M = max(Counter.values())
m = min(Counter.values()) if len(Counter) == (A+1)*(B+1) else 0
print(m,M)
