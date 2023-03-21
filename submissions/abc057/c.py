N = int(input())

def F(A,B):
    A, B = str(A), str(B)
    return len(A) if len(A) > len(B) else len(B)

def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i !=  n//i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

dl1 = make_divisors(N)
dl2 = dl1[::-1]
ans = 10
for d1, d2 in zip(dl1, dl2):
    f = F(d1,d2)
    if ans > f:
        ans = f
    if d1 >= d2:
        break
print(ans)
