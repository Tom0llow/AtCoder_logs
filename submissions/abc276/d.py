import collections
import math

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

N = int(input())
A = list(map(int,input().split()))

GCD = math.gcd(A[0],A[1])
for i in range(2,N):
    GCD = math.gcd(A[i],GCD)

cnt = 0
for n in A:
    c = collections.Counter(prime_factorize(n//GCD))
    for k,v in c.items():
        if k in [2,3]:
            cnt += v
        else:
            print(-1)
            exit()

print(cnt)
