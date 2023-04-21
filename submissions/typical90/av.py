N,K = map(int,input().split())

L = []
for _ in range(N):
    a,b = map(int,input().split())
    L.append(b)
    L.append(a-b)

L.sort(reverse=True)
ans = 0
for i in range(K):
    ans += L[i]

print(ans)
