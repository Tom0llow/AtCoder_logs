H,W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]

row = [0]*H
col = [0]*W
for i in range(H):
    row[i] = sum(A[i])
    for j in range(W):
        col[j] += A[i][j]

ans = [[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        ans[i][j] = (row[i]+col[j]) - A[i][j]


for a in ans:
    print(*a)
