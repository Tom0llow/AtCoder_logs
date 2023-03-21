N = int(input())
p = list(map(int, input().split()))

max_score = sum(p)
dp = [[0 for _ in range(max_score+1)] for _ in range(N)]

for j in range(max_score+1):
    if j >= p[0]:
        dp[0][j] = p[0]

for i in range(1, N):
    for j in range(max_score+1):
        tmp_not_choice = dp[i-1][j]
        if j < p[i]:
            dp[i][j] = tmp_not_choice
        else:
            tmp_choice = dp[i-1][j-p[i]] + p[i]
            dp[i][j] = max(tmp_not_choice, tmp_choice)

# for d in dp:
#     print(d)

ans = len(set(dp[-1]))
print(ans)
