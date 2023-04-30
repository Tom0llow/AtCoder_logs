H,W = map(int,input().split())
A = [input() for _ in range(H)]
B = [input() for _ in range(H)]

for s in range(H):
    for t in range(W):
        flag = True
        for i in range(H):
            for j in range(W):
                if A[(i-s+H) % H][(j-t+W) % W] != B[i][j]:
                    flag = False
        
        if flag:
            print('Yes')
            exit()

print('No')
