N,M = map(int,input().split())
X = list(map(int,input().split()))

X.sort()

d = []
for i in range(M-1):
    d.append(X[i+1] - X[i])
d.sort()

ans = 0
cnt = max(0,M-N)
for i in range(cnt):
    ans += d[i]

print(ans)
