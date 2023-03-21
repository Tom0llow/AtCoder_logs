H,W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]

cnt = 0
def dfs(nx,ny,path):
    global cnt 

    if (nx,ny) == (H-1,W-1):
        # print(path)
        if len(path) == len(set(path)): 
            cnt += 1
        return cnt 
    
    for (i,j) in [(0,1),(1,0)]:
        nx,ny = nx+i,ny+j
        
        if nx <= H-1 and ny <= W-1:
            path.append(A[nx][ny])
            dfs(nx,ny,path)
            path.pop()

        nx,ny = nx-i,ny-j


(dfs(0,0,[A[0][0]]))
print(cnt)
