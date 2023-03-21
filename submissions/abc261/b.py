N = int(input())
A = []
for _ in range(N):
    a = input()
    A.append(a)

ans = 'correct'
for i in range(N):
    for j in range(N):
        if A[i][j] == '-':
            continue
        if A[i][j] == 'W' and A[j][i] == 'L':
            continue
        if A[i][j] == 'L' and A[j][i] == 'W':
            continue
        if A[i][j] == 'D' and A[j][i] == 'D':
            continue
        ans = 'incorrect'
        break

print(ans)
