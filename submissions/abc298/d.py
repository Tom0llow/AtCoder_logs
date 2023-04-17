from collections import deque

MOD = 998244353
S = deque([1])
ans = 1

Q = int(input())

for _ in range(Q):
    query = list(map(int,input().split()))
    
    if query[0] == 1:
        x = query[1]
        S.append(x)
        ans = (ans*10 + x) % MOD
        
    elif query[0] == 2:
        ans = (ans - pow(10,len(S)-1,MOD) * S.popleft()) % MOD
    
    else:
        print(ans)
    
