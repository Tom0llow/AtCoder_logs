N = int(input())
M = [[0]*1001 for _ in range(1001)]
for _ in range(N):
    lx,ly,rx,ry = map(int,input().split())

    for y in range(ly,ry):
        M[y][lx] += 1
        M[y][rx] -= 1


ans = [0]*(N+1)
for y in range(1001):
    for x in range(1000): 
        M[y][x+1] += M[y][x]
        m = M[y][x]
        ans[m] += 1

print(*ans[1:], sep='\n')
