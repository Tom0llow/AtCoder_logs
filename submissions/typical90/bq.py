MOD = 1000000007

N,K = map(int,input().split())

if N == 1:
    ans = K % MOD
else:
    ans = K%MOD * (K-1)%MOD * pow(K-2, N-2, MOD)%MOD

print(ans)


 
