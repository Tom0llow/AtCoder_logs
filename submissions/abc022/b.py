from collections import defaultdict

N = int(input())

A = defaultdict(int)
for _ in range(N):
    a = int(input())
    A[a] += 1

ans = 0
for k,v in A.items():
    if v > 1:   ans += v-1

print(ans)  
