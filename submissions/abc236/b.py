from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

ad = defaultdict(int)
for a in A:
    ad[a] += 1

ans = min(ad, key=ad.get)
print(ans)
