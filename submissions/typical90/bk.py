from itertools import product
from collections import defaultdict


H,W = map(int,input().split())
P = [list(map(int,input().split())) for _ in range(H)]

def count(pro):
    d = defaultdict(int)
    d[0] = 1

    Grid = []
    for i in range(H):
        if pro[i]:
            Grid.append(P[i])
    
    if not Grid:    return 0
    
    for j in range(W):
        flag = True
        for i in range(len(Grid)-1):
            if Grid[i][j] != Grid[i-1][j]:
                flag = False
                break
        if flag:
            d[Grid[0][j]] += len(Grid)

    # print(Grid)
    return max(d.values())


ans = 1
for pro in product([0,1], repeat=H):
    ans = max(ans,count(pro))

print(ans)
