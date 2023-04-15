N = int(input())
A = list(map(int,input().split()))
cnt = [0]*3
for a in A:
    cnt[a-1] += 1

dp = [[[0 for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]
for z in range(N+1):
    for y in range(N+1):
        for x in range(N+1):
            M = x+y+z
            if M>N or M==0: continue
            dp[x][y][z] += x * dp[x-1][y][z] if x > 0 else 0
            dp[x][y][z] += y * dp[x+1][y-1][z] if y > 0 else 0
            dp[x][y][z] += z * dp[x][y+1][z-1] if z > 0 else 0
            dp[x][y][z] = (dp[x][y][z] + N) / M

print(dp[cnt[0]][cnt[1]][cnt[2]])
