from bisect import bisect_left

N,M,D = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort()

ans = -1
for a in A:
    i = bisect_left(B,a+D)

    if i > M-1: i -= 1    
    if abs(B[i] - a) <= D:   ans = max(ans, a+B[i])
    if abs(B[i-1] - a) <= D:  ans = max(ans, a+B[i-1])

print(ans)
