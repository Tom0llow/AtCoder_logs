N = int(input())
S = str(input())
W = list(map(int, input().split()))

WS = []
for i in range(N):
    WS.append([W[i],S[i]])
sort_WS = sorted(WS, key=lambda x: x[0])

S = [None]*N
for i in range(N):
    w, s = sort_WS[i]
    W[i], S[i] = w, s

ans = S.count('1') 
X = ans
for i in range(N):
    if S[i] == '1': X -= 1
    else:   X += 1

    if i < N-1:
        if W[i] != W[i+1]:  ans = max(ans, X)
    else:   ans = max(ans, X)

print(ans)
