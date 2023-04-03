MOD = 10**9+7

H,W = map(int,input().split())
a = [input() for _ in range(H)]

dp = [[0 for _ in range(W)] for _ in range(H)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:   continue
        if a[i][j] == '#':  dp[i][j] = 0
        else:   dp[i][j] = (dp[i-1][j]+dp[i][j-1]) % MOD

print(dp[H-1][W-1])
