H,W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
B = [list(map(int,input().split())) for _ in range(H)]


D = [[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        D[i][j] = A[i][j] - B[i][j]
# print(*D, sep='\n')


cnt = 0
for i in range(H-1):
    for j in range(W-1):
        if D[i][j] == 0:    continue
        
        d = -D[i][j] 
        D[i][j] += d 
        D[i+1][j] += d
        D[i][j+1] += d
        D[i+1][j+1] += d
        
        cnt += d if d > 0 else -d
# print(*D, sep='\n')


flag = True
for i in range(H):
    for j in range(W):
        if D[i][j] != 0:    
            flag = False
            break

if flag:
    print('Yes')
    print(cnt)
else:
    print('No')
