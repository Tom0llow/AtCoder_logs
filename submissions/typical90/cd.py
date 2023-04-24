MOD = 1000000007


L,R = map(int,input().split())

def mod_calc(a1, an, n):
    return ((an-a1+1)*(a1+an))//2 %MOD * n%MOD

ans = 0
nL = len(str(L))
nR = len(str(R))
a1 = L
for n in range(nL, nR+1):
    if nR > n:
        ans += mod_calc(a1, pow(10,n)-1, n)
    else:
        ans += mod_calc(a1, R, n)

    ans %= MOD
    a1 = pow(10,n)


print(ans)
