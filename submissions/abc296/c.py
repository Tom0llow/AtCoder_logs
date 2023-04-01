import bisect

N,X = map(int,input().split())
A = list(map(int,input().split()))

A.sort()
for a in A:
    id = bisect.bisect_right(A, a+X)
    if A[id-1] == a+X:
        print('Yes')
        exit()

print('No')        
