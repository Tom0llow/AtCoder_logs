N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

cnt = 0
for a,b in zip(A,B):
    cnt += abs(a-b)

ans = 'No'
if cnt == K or (cnt < K and (K-cnt) % 2 == 0):
    ans = 'Yes'

print(ans)
