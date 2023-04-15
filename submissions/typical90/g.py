import bisect

N = int(input())
A = list(map(int,input().split()))
Q = int(input())
B = [int(input()) for _ in range(Q)]

A.sort()
# print(A)
for b in B:
    i = bisect.bisect_left(A,b)
    if 0 < i < N:   i -= 1
    elif i == N:    i -= 2
    
    if N == 1:  ans = abs(b-A[i])
    else:   ans = min(abs(b-A[i]), abs(b-A[i+1]))
    print(ans)
 
