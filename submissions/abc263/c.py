def dfs(A):
    if len(A) == N:
        flag = True
        for i in range(N-1):
            if not A[i] < A[i+1]: 
                flag = False
                break
        if flag:        
            print(' '.join(map(str,A)))
        return
    prev_last = A[-1] if len(A) > 0 else 1
    for v in range(prev_last,M+1):
        A.append(v)
        dfs(A)
        A.pop()

N, M = map(int, input().split())

dfs([])
