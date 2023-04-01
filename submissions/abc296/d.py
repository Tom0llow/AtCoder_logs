N,M = map(int,input().split())

if N*N < M:
    print(-1)
    exit()

ans = N*N
for a in range(1,int(max(N,M)**0.5)+2):
    b = -(-M//a)
    if 1 <= b <= N:
        ans = min(ans,a*b)
    
print(ans)
