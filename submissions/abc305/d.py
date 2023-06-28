import bisect


N = int(input())
A = list(map(int,input().split()))
Q = int(input())
q = [list(map(int,input().split())) for _ in range(Q)]


sumA = [0]*N
for i in range(N-1):
    if (i+1) % 2 == 0:  sumA[i+1] = sumA[i] + (A[i+1] - A[i])
    else:   sumA[i+1] = sumA[i]

# print(sumA)

for l,r in q:
    i = bisect.bisect_right(A,l)
    j = bisect.bisect_left(A,r)
    
    ans = 0
    if i % 2 == 0:  ans += A[i] - l
    if j % 2 == 0:  ans += r - A[j]
    ans += sumA[j] - sumA[i]

    print(ans)
