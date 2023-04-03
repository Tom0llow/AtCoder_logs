N = int(input())
p = list(map(float,input().split()))
p = [0]+p

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
dp[0][0] = 1
for i in range(1,N+1):
    for j in range(i+1):
        if j > 0:   dp[i][j] = dp[i-1][j]*(1-p[i]) + dp[i-1][j-1]*p[i]
        else:   dp[i][j] = dp[i-1][j]*(1-p[i])

# print(*dp, sep='\n')

ans = 0
for j in range(N//2+1,N+1):
    ans += dp[N][j]
print(ans)
