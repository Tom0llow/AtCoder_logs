from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
M = max(A)

c = defaultdict(int)
for i in range(N):
    c[A[i]] += 1 

ans = 0
for q in range(1, M+1):
    r = 1
    while q*r <= M:
        ans += c[q] * c[r] * c[q*r]
        r += 1

print(ans)
