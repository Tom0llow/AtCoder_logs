from itertools import permutations

INF = float('inf')

N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]

M = int(input())
kenaku = [[False]*(N+1) for _ in range(N+1)]
for _ in range(M):
    X,Y = map(int,input().split())
    kenaku[X][Y] = True
    kenaku[Y][X] = True


ans = INF
for permutation in permutations(range(1,N+1)):
    flag = True    
    time = 0
    for i in range(N):    
        if i < N-1 and kenaku[permutation[i]][permutation[i+1]]:  
            flag = False
            break

        time += A[permutation[i]-1][i]    
    
    if flag:    ans = min(ans, time)


ans = -1 if ans == INF else ans
print(ans)
