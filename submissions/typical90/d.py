from collections import defaultdict

H,W = map(int,input().split())
A = []
row = []
c = defaultdict(list)
for i in range(H):
    a = list(map(int,input().split()))
    A.append(a)
    row.append(sum(a))
    for j in range(W):
        c[j].append(a[j])
col = []
for j in range(W):
    col.append(sum(c[j]))


B = [[0 for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        s = row[i]+col[j]
        B[i][j] = s-A[i][j]

for b in B:
    print(*b)
