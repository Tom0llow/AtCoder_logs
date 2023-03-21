from collections import defaultdict

N = int(input())

sdict = defaultdict(int)

for i in range(N):
    S = str(input())
    sdict[S] += 1

ans = ''
max = 0
for k, v in sdict.items():
    if max < v:
        ans = k
        max = v

print(ans)
