N, K, X = map(int, input().split())
A = list(map(int, input().split()))

def coupon(a, k):
    return max(a-k*X, 0)

for i in range(N):
    if A[i] >= X:
        m = min(A[i] // X, K)
        A[i] = coupon(A[i], m)
        K -= m

if K >= N:
    ans = 0
else:
    A = sorted(A, reverse=True)
    for i in range(K):
        A[i] = 0
        K -= 1    
    ans = sum(A)

print(ans)
