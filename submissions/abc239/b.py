X = int(input())

if 0 <= X < 10:
    ans = 0 
elif -10 < X <= 0:
    ans = -1
elif X >= 10:
    X = str(X)    
    ans = X[:-1]
else:
    X = str(X)
    ans = X[:-1]
    if X[-1] != '0':
        ans = int(ans) - 1

print(ans)
