N,K =map(int,input().split())
h = list(map(int,input().split()))

dp = [0]*N
dp[0] = 0
dp[1] = abs(h[1]-h[0])

for i in range(2,N):
    dp[i] = dp[i-1]+abs(h[i]-h[i-1])
    for j in range(2,K+1):
        if i-j >= 0:
            dp[i] = min(dp[i-j]+abs(h[i]-h[i-j]),dp[i])

print(dp[-1])
