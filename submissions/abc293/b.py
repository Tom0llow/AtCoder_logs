N = int(input())
A = list(map(int,input().split()))

X = list(range(1,N+1))
for i in range(N):
    if X[i] != 0:
        X[A[i]-1] = 0
        
X = [x for x in sorted(X) if x > 0]
print(len(X))
print(*X)
