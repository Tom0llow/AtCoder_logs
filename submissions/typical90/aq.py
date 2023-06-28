from collections import deque



INF = float('inf')


H,W = map(int,input().split())
rs,cs = map(int,input().split())
rt,ct = map(int,input().split())
S = [input() for _ in range(H)]


rs,cs,rt,ct = rs-1,cs-1,rt-1,ct-1

# dist = [[[INF]*4 for _ in range(W)] for _ in range(H)]
dist = [INF for _ in range(4*H*W)]

que = deque()
for k in range(4):
    dist[4*(rs*W+cs) + k] = 0
    que.append([rs,cs,k])

d = [[1, 0], [-1, 0], [0, 1], [0, -1]]

while que:
    x,y,v = que.popleft()

    for k in range(4):
        i,j = d[k]
        nx,ny = x+i,y+j
        nv = k

        if (not 0 <= nx < H) or (not 0 <= ny < W):  continue
        if S[nx][ny] == '#':    continue

        c = 0 if v == nv else 1
        if dist[4*(nx*W+ny) + nv] > dist[4*(x*W+y) + v] + c:
            dist[4*(nx*W+ny) + nv] = dist[4*(x*W+y) + v] + c

            if v == nv: que.appendleft([nx,ny,nv])
            else:   que.append([nx,ny,nv])


print(min([dist[4*(rt*W+ct) + k] for k in range(4)]))
