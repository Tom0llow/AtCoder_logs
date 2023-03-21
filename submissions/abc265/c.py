import sys


H, W = map(int,input().split())
G = [[c for c in input()] for _ in range(H)]

i,j = 0,0
while True:
    if G[i][j] == 'U' and i+1 != 1:
        G[i][j] = '*'
        i -= 1
    elif G[i][j] == 'D' and i+1 != H:
        G[i][j] = '*'
        i += 1
    elif G[i][j] == 'L' and j+1 != 1:
        G[i][j] = '*'
        j -= 1
    elif G[i][j] == 'R' and j+1 != W:
        G[i][j] = '*'
        j += 1
    elif G[i][j] == '*':
        print(-1)
        sys.exit()
    else:
        ans = (i+1,j+1)
        break

print(*ans, sep=' ')
    
