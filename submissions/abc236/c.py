from collections import defaultdict

N, M = map(int, input().split())
S = list(map(str, input().split()))
T = list(map(str, input().split()))

dict = defaultdict(int)
for s in S:
    dict[s] += 1
for t in T:
    dict[t] += 1

for k, v in dict.items():
    if v == 2:
        print('Yes')
    else:
        print('No')
