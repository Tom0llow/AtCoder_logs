import math

T = int(input())
for _ in range(T):
    N,D,K = map(int,input().split())

    K -= 1
    a = N / math.gcd(N,D)
    print(int(D*K%N + K/a))
