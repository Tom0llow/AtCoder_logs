N, L, R = map(int,input().split())
A = list(map(int,input().split()))

A.insert(0,0)
f = [0]*(N+1)
f[0] = 0
for k in range(N):
    f[k+1] = min((f[k])+A[k+1], L*(k+1))    

g = [0]*(N+1)
for k in range(N):
    g[k+1] = min((g[k]+A[N-k]), R*(k+1))    

ans = sum(A)
for i in range(N+1):
    ans = min(ans, f[i]+g[N-i])

print(ans)
