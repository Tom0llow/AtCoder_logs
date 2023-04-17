N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
B = [list(map(int,input().split())) for _ in range(N)]


for _ in range(4):
    L = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            L[j][N-1-i] = A[i][j]
    A = L.copy()
    # print(*A, sep='\n')

    flag = True
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1:
                if B[i][j] == 1:    continue
                else:   flag = False
    if flag:
        print('Yes')
        exit()

print('No') 
