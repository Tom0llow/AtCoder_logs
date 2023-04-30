def sieve_of_eratosthenes(x):
    nums = [i for i in range(x+1)]

    root = int(pow(x,0.5))
    for i in range(2,root + 1):
        if nums[i] != 0:
            for j in range(i, x+1):
                if i*j >= x+1:
                    break
                nums[i*j] = 0

    primes = sorted(list(set(nums)))[2:]

    return primes


N = int(input())


ans = 0
P = sieve_of_eratosthenes(3 * pow(10,5))
for i in range(len(P)):
    if P[i]**2 * P[i+1] * P[i+2]**2 > N:   break
    
    for j in range(i+1,len(P)):
        if P[i]**2 * P[j] * P[j+1]**2 > N:   break
        
        for k in range(j+1,len(P)):
            v = P[i]**2 * P[j]
            if v > N:   break
            v *= P[k]
            if v > N:   break
            v *= P[k]
            if v > N:   break

            ans += 1

print(ans)
