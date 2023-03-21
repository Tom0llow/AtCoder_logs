N = int(input())
X = list(map(int,input().split()))

X = sorted(X)
X = X[N:4*N]
# print(X)

print(sum(X)/(3*N))
