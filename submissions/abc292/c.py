N = int(input())


def divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


cnt = 0
for x in range(1,N+1):
    # print(x)
    # print(divisors(x))
    # print(divisors(N-x))
    cnt += len(divisors(x)) * len(divisors(N-x))

print(cnt)


