H, W = map(int, input().split())
S = []
Start, Goal = 0, 0 
for i in range(H):
    s = input()
    S.append(s)
    for j in range(W):
        if s[j] == 'o':
            if not Start:
                Start = (i, j)
            else:
                Goal = (i, j)

ans = abs(Start[0]-Goal[0]) + abs(Start[1]-Goal[1])
print(ans)
