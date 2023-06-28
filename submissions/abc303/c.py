N,M,H,K = map(int,input().split())
S = input()

G = set()
for _ in range(M):
    x,y = map(int,input().split())
    G.add((x,y))

x,y = 0,0
for s in S:
    if s == 'R':    x,y = x+1,y        
    elif s =='L':   x,y = x-1,y
    elif s == 'U':  x,y = x,y+1
    elif s == 'D':  x,y = x,y-1

    H -= 1
    if H >= 0:
        if (x,y) in G and H < K:
            H = K
            G.remove((x,y))

    else:
        print('No')
        exit()

print('Yes')
    



