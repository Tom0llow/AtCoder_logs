K = int(input())

def make_divisors(n):
    l,u = [],[]
    i = 1
    while i*i <= n:
        if n % i == 0:
            l.append(i)
            if i != n // i:
                u.append(n // i)
        i += 1
    return l + u[::-1]


d = make_divisors(K)

ans = 0
for a in d:
    for b in d:
        c = K / (a*b)
        if a <= b <= c and K % (a*b) == 0:
            ans += 1 

print(ans)
