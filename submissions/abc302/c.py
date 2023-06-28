import itertools


N,M = map(int,input().split())
S = [input() for _ in range(N)]

for T in itertools.permutations(S,N):
    flag = True
    for i in range(N-1):
        cnt = 0
        for j in range(M):
            if T[i][j] != T[i+1][j]:    cnt += 1

        if cnt > 1: 
            flag = False
            break
    
    if flag:
        print('Yes')
        exit()


print('No')
