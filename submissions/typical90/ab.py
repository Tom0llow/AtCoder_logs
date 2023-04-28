N = int(input())

papers = [[0]*1001 for _ in range(1001)]

# �d�݂̉��Z
for _ in range(N): 
    lx,ly,rx,ry = map(int,input().split())

    papers[ly][lx] += 1
    papers[ly][rx] -= 1
    papers[ry][lx] -= 1
    papers[ry][rx] += 1

# �������ւ̗ݐϘa
for y in range(0,1001):
    for x in range(1,1001):
        papers[y][x] += papers[y][x-1]

# �c�����ւ̗ݐϘa
for y in range(1,1001):
    for x in range(0,1001):
        papers[y][x] += papers[y-1][x]

ans = [0]*(N+1)
for y in range(0,1001):
    for x in range(0,1001):
        k = papers[y][x]
        ans[k] += 1

print(*ans[1:], sep='\n')
