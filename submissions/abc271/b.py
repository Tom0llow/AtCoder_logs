N,Q = map(int,input().split())

A = []
for _ in range(N):
    a = list(map(int,input().split()))
    A.append(a[1:])

for _ in range(Q):
    s,t = map(int,input().split())
    print(A[s-1][t-1])
