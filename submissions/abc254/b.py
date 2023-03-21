N = int(input())

A = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if j == 0 or j == i:
            A[i][j] = 1
        else:
            A[i][j] = A[i-1][j-1] + A[i-1][j]
            
for i in range(N):
    A[i] = A[i][:i+1]
    print(*A[i], sep=' ')
     
