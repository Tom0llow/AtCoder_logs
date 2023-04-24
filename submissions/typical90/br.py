N = int(input())

X = [0]*N
Y = [0]*N
for i in range(N):
    X[i],Y[i] = map(int,input().split())

X.sort()
Y.sort()

if N % 2 == 1:
    a = X[N//2]
    b = Y[N//2]
else:
    a = (X[N//2] + X[N//2-1]) // 2
    b = (Y[N//2] + Y[N//2-1]) // 2

ansA = sum([abs(x-a) for x in X])
ansB = sum([abs(y-b) for y in Y])

print(ansA+ansB)
