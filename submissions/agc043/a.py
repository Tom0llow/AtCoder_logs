INF = float('inf')
H,W = map(int,input().split())
G = [list(input()) for _ in range(H)]

dp = [[INF for _ in range(W)] for _ in range(H)]
if G[0][0] == '.':
    dp[0][0] = 0
else:
    dp[0][0] = 1

for i in range(H):
    for j in range(W):
        D = []
        if i != 0:
            D.append([0,-1])
        if j != 0:
            D.append([-1,0])

        for x,y in D:
            if G[i][j] == '#' and G[i+y][j+x] == '.':
                dp[i][j] = min(dp[i][j], dp[i+y][j+x]+1)
            else:
                dp[i][j] = min(dp[i][j], dp[i+y][j+x])

print(dp[H-1][W-1])
