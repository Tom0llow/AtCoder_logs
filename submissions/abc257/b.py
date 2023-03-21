N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for i in range(Q):
    if N != A[L[i]-1]:
        if A[L[i]-1] == A[-1] or A[L[i]] != A[L[i]-1]+1: 
            A[L[i]-1] += 1
print(*A, sep=' ') 
