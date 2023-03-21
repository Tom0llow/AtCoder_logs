N = int(input())
# DP 配列を用意する
# 本問では i 日目の動作として「Aをやる」「Bをやる」「Cをやる」の3通りが考えられる
# それぞれの行動をするための最大幸福度をそれぞれの漸化式で求める
# i 日目に A、B、C をやるための最大幸福度は dp[i][0]、dp[i][1]、dp[i][2] とする
dp = [[0]*3 for _ in range(N+1)]

# 初期条件を入力
dp[0][0] = 0
dp[0][1] = 0
dp[0][2] = 0

for i in range(1, N+1):
    a, b, c = map(int, input().split())
    dp[i][0] = max(dp[i-1][1]+a, dp[i-1][2]+a)
    dp[i][1] = max(dp[i-1][0]+b, dp[i-1][2]+b)
    dp[i][2] = max(dp[i-1][0]+c, dp[i-1][1]+c)

# for d in dp:
#     print(d)

ans = max(dp[-1])
print(ans)
