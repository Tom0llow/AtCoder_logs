from collections import deque

INF = float('inf')

H,W = map(int,input().split())
rs,cs = map(lambda x: int(x)-1, input().split())
rt,ct = map(lambda x: int(x)-1, input().split())
S = [input() for _ in range(H)]

# dist = [[[INF]*W for _ in range(H)] for _ in range(4)] -> TLE
dist = [INF for _ in range(4*H*W)]

que = deque([])
for k in range(4):
    dist[4*(rs*W+cs) + k] = 0
    que.append((rs,cs,k))

dir = [[1,0], [-1,0], [0,1], [0,-1]]

while que:
    x,y,d = que.popleft()

    for k in range(4):
        i,j = dir[k]
        nx = x+i
        ny = y+j
        nd = k

        if nx >= H or nx < 0 or ny >= W or ny < 0:  continue
        if S[nx][ny] == '#':  continue
        
        c = 0 if d == nd else 1

        if dist[4*(nx*W+ny) + nd] > dist[4*(x*W+y) + d] + c:
            dist[4*(nx*W+ny) + nd] = dist[4*(x*W+y) + d] + c

            if d == nd: que.appendleft((nx,ny,nd))
            else:   que.append((nx,ny,nd))


# print(dist)
ans = min([dist[4*(rt*W+ct) + k] for k in range(4)])
print(ans)
