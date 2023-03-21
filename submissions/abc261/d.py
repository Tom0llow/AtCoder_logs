N, M = map(int, input().split())
X = list(map(int, input().split()))
X.insert(0,0)
b = [0]*(N+1)
for i in range(M):
    C, Y = map(int, input().split())
    b[C] = Y

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
dp[0][0] = 0

for i in range(1,N+1):
    for j in range(1,N+1):
        dp[i][j] = dp[i-1][j-1] + X[i] + b[j]
    
    dp[i][0] = 0
    for j in range(i):
        dp[i][0] = max(dp[i][0], dp[i-1][j])

ans = max(dp[N])
print(ans)
