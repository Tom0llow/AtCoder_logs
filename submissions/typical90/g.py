import bisect

N = int(input())
A = list(map(int,input().split()))
Q = int(input())
B = [int(input()) for _ in range(Q)]


A.sort()
for b in B:
    l = bisect.bisect_left(A,b)
    l = l if l < N else l-1
    ans = min(abs(A[l]-b), abs(A[l-1]-b))

    print(ans)
