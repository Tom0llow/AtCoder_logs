N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

p = 0
for b in B:
    p += A[b-1]

print(p)
