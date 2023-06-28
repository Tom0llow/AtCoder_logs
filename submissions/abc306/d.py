N = int(input())
XY = [list(map(int,input().split())) for _ in range(N)]

dp = [[0]*2 for _ in range(N+1)]
dp[0][0] = 0

for i in range(1,N+1):
    Xi,Yi = XY[i-1]
    if Xi == 0:
        dp[i][0] = max(dp[i-1][0], dp[i-1][0] + Yi, dp[i-1][1] + Yi)
        dp[i][1] = dp[i-1][1]    

    else:
        dp[i][0] = dp[i-1][0]
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] + Yi)   


# print(*dp, sep='\n')
print(max(dp[N]))
