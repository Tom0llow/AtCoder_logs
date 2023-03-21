N, M = map(int, input().split())
ng = [False]*(N+1)
for _ in range(M):
    a = int(input())
    ng[a] = True

dp = [0]*(N+1)
dp[0] = 1

for i in range(N):
    if not ng[i+1]:
        dp[i+1] += dp[i]
    if i+2 < len(dp):
        if not ng[i+2]:
            dp[i+2] += dp[i]

div = 1000000007    
ans = dp[-1] % div

print(ans)
