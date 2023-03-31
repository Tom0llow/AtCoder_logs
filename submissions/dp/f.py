s = input()
t = input()

dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
for i in range(1,len(s)+1):
    for j in range(1,len(t)+1):
        if s[i-1] == t[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

# print(*dp, sep='\n')

lenDP = dp[len(s)][len(t)]
i = len(s)-1
j = len(t)-1
ans = ['']*lenDP
while lenDP > 0:
    if s[i] == t[j]:
        ans[lenDP-1] = s[i]
        i -= 1
        j -= 1
        lenDP -= 1
    elif dp[i+1][j+1] == dp[i][j+1]:
        i -= 1
    else:
        j -= 1

print(*ans, sep='')
