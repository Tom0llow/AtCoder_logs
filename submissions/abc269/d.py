N = int(input())
xy = set([tuple(map(int,input().split())) for _ in range(N)])
move = [[-1,-1], [-1,0], [0,-1], [0,1], [1,0], [1,1]]

done = set()
ans = 0

for x,y in xy:
    if (x,y) in done:
        continue
    todo = [(x,y)]
    done.add((x,y))
    ans += 1
    
    while todo:
        nx,ny = todo.pop()
        for di,dj in move:
            if (nx+di,ny+dj) not in xy or (nx+di,ny+dj) in done:
                continue
            todo.append((nx+di,ny+dj))
            done.add((nx+di,ny+dj))

print(ans)
