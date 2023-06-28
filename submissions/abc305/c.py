H,W = map(int,input().split())
S = [input() for _ in range(H)]


row_num = []
for i in range(H):
    row_num.append(S[i].count('#'))


col_num = [0]*W
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            col_num[j] += 1

# print(row_num)
# print(col_num)
for i in range(H):
    if 0 < row_num[i] < max(row_num):   break

for j in range(W):
    if 0 < col_num[j] < max(col_num):   break


print(i+1,j+1)

