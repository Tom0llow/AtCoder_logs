from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

s = 0
dd = defaultdict(int)
dd[0] = 1
ans = 0

for i in range(N):
    s += A[i]
    ans += dd[s-K]
    dd[s] += 1
    
print(ans)
