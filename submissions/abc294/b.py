H,W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]

for i in range(H):
    S = ''
    for j in range(W):
        S += '.' if A[i][j] == 0 else chr(ord('A')+A[i][j]-1)
    print(S)
        
