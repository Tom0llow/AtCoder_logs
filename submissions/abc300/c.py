H,W = map(int,input().split())
C = [input() for _ in range(H)]

def ok(i,j):
    return 0 <= i < H and 0 <= j < W

def judge(i, j, d):
    for x in [d,-d]:
        for y in [d,-d]:
            s = i+x
            t = j+y
            if (not ok(s,t)) or C[s][t] != '#':
                return False
    return True

N = min(H,W)
ans = [0]*N
for a in range(H):
    for b in range(W):
        if C[a][b] != '#':  continue
        if judge(a, b, 1):
            d = 1
            while judge(a, b, d+1):
                d += 1
            
            ans[d-1] += 1

print(*ans)
