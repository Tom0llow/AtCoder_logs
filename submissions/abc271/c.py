N = int(input())
a = list(map(int,input().split()))

vol = [False for _ in range(N+2)]
sold = 0
for i in range(N):
    if a[i] >= len(vol):    sold += 1
    elif vol[a[i]]: sold += 1
    else: vol[a[i]] = True

L = 1
R = N+1
while True:
    while vol[L]:   L += 1
    while R != 0 and not vol[R]:    R -= 1
    if sold >= 2:
        sold -= 2
        vol[L] = True
    else:
        if L >= R:  break
        vol[R] = False
        sold += 1
    
print(L-1)
