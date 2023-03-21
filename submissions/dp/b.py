N, K = map(int, input().split())
h = list(map(int, input().split()))

# DP 配列を用意
# dp[i] には i 番目の足場にたどり着くために必要な最低コストを入れる
dp = [0]*N

# 初期条件を入力
dp[0] = 0

# 漸化式にしたがってループを回す
for i in range(1, N):
    # i を現在いる足場と考える
    # i 番目の足場へ行く方法は max(K, i-K) 通りある
    # それぞれの生き方にかかるコストを tmp (temporary) にまとめる
    tmp = []
    for j in range(max(0, i-K), i):
        tmp.append(abs(h[j]-h[i]) + dp[j])
    # tmp のうち最小コストを dp[i] とする
    # print(tmp)
    dp[i] = min(tmp)

# dp 配列の末尾が N 番目の足場に辿り着くために必要なコストとなる
# print(dp)
print(dp[-1])
