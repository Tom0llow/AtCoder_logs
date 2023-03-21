Q = int(input())

n = 101010
is_prime = [1 for _ in range(n)]
is_prime[0] = 0
is_prime[1] = 0
for i in range(2,n):
    if not is_prime[i]: continue
    for j in range(i*2,n,i):
        is_prime[j] = 0

a = [0]*n
for i in range(n):
    if i%2 == 0: continue
    if is_prime[i] and is_prime[(i+1)//2]: a[i] = 1

S = [0]*(n+1)
for i in range(n):
    S[i+1] = S[i]+a[i]

for _ in range(Q):
    l,r = map(int,input().split())
    print(S[r+1]-S[l])
