N,Q = map(int,input().split())

p = [0 for _ in range(N+1)]
for _ in range(Q):
    c,x = map(int,input().split())
    if c == 1:
        p[x] += 1
    elif c == 2:
        p[x] += 2
    else:
        ans = 'Yes' if p[x] >= 2 else 'No'
        print(ans)
