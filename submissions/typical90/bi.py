Q = int(input())

d1 = []
d2 = []
for _ in range(Q):
    t,x = map(int,input().split())

    if t == 1:
        d1.append(x)

    elif t == 2:
        d2.append(x)

    else:
        if x <= len(d1):
            print(d1[-x])
        else:
            print(d2[(x-len(d1))-1])
