T = int(input())
for _ in range(T):
    N = int(input())

    prime_factors = []
    for p in range(2, int(N**0.5)+1):
        if N % p == 0:
            prime_factors.append(p)
            N //= p
            break
    
    if N % p == 0:
        prime_factors.append(N//p)
    else:   
        prime_factors.append(int(N**0.5))
        prime_factors.reverse()

    print(*prime_factors)
