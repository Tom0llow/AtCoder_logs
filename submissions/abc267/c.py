N,M = map(int,input().split())
A = list(map(int,input().split()))

S = [0]*(N+1)
for i in range(1,N):
    S[i] = S[i-1]+A[i-1]

Si = [0]*(N-M+1)
now = 0
for i in range(M):
    now += A[i]*(i+1)
Si[0] = now

for i in range(1,N-M+1):
   Si[i] = Si[i-1] + M*A[M+i-1] - (S[M+i-1]-S[i-1]) 

ans = -float('inf')
for i in range(N-M+1):
    ans = max(ans,Si[i])

print(ans)
