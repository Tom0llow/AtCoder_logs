import itertools
from collections import defaultdict

N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
M = int(input())
XY = defaultdict(list)
for _ in range(M):
    X,Y = map(int,input().split())
    XY[X].append(Y)
    XY[Y].append(X)


L = list(itertools.permutations(list(range(1,N+1))))
INF = float('inf')
ans = INF
for l in L: 
    flag = True
    cnt = 0
    for i in range(N-1):   
        if l[i+1] in XY[l[i]]: 
            flag = False
            break
        cnt += A[l[i]-1][i]    
    cnt += A[l[-1]-1][-1]        
    
    if flag:
        ans = min(ans,cnt)

if ans == INF:  ans = -1
print(ans)
