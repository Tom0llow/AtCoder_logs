INF = float('inf')

N,W = map(int,input().split())
wv = [tuple(map(int,input().split())) for _ in range(N)]

VMAX = 10**3 * N

dp = [[INF for _ in range(VMAX+1)] for _ in range(N+1)]
dp[0][0] = 0

for i in range(1,N+1):
    w,v = wv[i-1]
    for j in range(0,VMAX+1):
        if j-v >= 0:
            dp[i][j] = min(dp[i-1][j-v]+w, dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

for j in range(VMAX,1,-1):
    if dp[N][j] <= W:
        print(j)
        exit()
