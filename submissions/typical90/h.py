MOD = 1000000007


N = int(input())
S = input()

s = 'atcoder'
dp = [[0]*(len(s)+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(1,N+1):
    for j in range(len(s)+1):
        dp[i][j] += dp[i-1][j]

        if S[i-1] == 'a' and j == 1:  dp[i][j] += dp[i-1][j-1]
        if S[i-1] == 't' and j == 2:  dp[i][j] += dp[i-1][j-1]
        if S[i-1] == 'c' and j == 3:  dp[i][j] += dp[i-1][j-1]
        if S[i-1] == 'o' and j == 4:  dp[i][j] += dp[i-1][j-1]
        if S[i-1] == 'd' and j == 5:  dp[i][j] += dp[i-1][j-1]
        if S[i-1] == 'e' and j == 6:  dp[i][j] += dp[i-1][j-1]
        if S[i-1] == 'r' and j == 7:  dp[i][j] += dp[i-1][j-1]
        
        dp[i][j] %= MOD


# print(*dp, sep='\n')
print(dp[N][len(s)])
