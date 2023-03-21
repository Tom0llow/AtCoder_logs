H,W = map(int,input().split())

l = [0 for _ in range(W)]
for _ in range(H):
    C = input()
    for j in range(W):
        if C[j] == '#':
            l[j] += 1

print(*l)
