N = int(input())
a = list(map(int, input().split()))

dp = [0]*N

dp[0] = 0
dp[1] = abs(a[1] - a[0])

for i in range(2, N):
    one_move = abs(a[i] - a[i-1]) + dp[i-1]
    two_move = abs(a[i] - a[i-2]) + dp[i-2]
    dp[i] = min(one_move, two_move)

# print(dp)
print(dp[-1])
