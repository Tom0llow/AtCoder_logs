N,L = map(int,input().split())
K = int(input())
A = list(map(int,input().split()))

def binary_search(l,r):
    if l == r:  return l
    M = (l+r+1)//2
    s = 0
    c = 0
    for i in range(N+1):
        if i == N:
            if L-s >= M:
                c += 1
        elif A[i]-s >= M:
            s = A[i]
            c += 1
        if c == K+1:
            # right part
            return binary_search(M,r)
    # left part
    return binary_search(l,M-1)

print(binary_search(0,L))
