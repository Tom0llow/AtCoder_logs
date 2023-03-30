N,W = map(int,input().split())
wv = [tuple(map(int,input().split())) for _ in range(N)]

dp = [[0 for _ in range(W+1)] for _ in range(N)]
w0,v0 = wv[0]
for j in range(w0,W+1):
    dp[0][j] = v0

for i in range(N):
    w,v = wv[i]
    for j in range(1,W+1):
        dp[i][j] = dp[i-1][j]
        if j-w >= 0:
            dp[i][j] = max(dp[i-1][j-w]+v, dp[i][j]) 

# print(*dp, sep='\n')
print(dp[N-1][W])
