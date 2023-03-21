N = int(input())
a = list(map(int, input().split()))

from collections import defaultdict
d = defaultdict(int)
for i in range(N):
    d[a[i]] += 1

print(len(d))
