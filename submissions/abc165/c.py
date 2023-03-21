N, M, Q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(Q)]

def score(A):
    pt = 0
    for i in range(Q):
        a, b, c, d = abcd[i][0], abcd[i][1], abcd[i][2], abcd[i][3]
        if A[b-1] - A[a-1] == c:
            pt += d
    return pt

def dfs(A):  
    if len(A) == N:
        return score(A)
    max_pt = 0
    last = A[-1] if len(A) > 0 else 0 
    for v in range(last, M):
        A.append(v)
        max_pt = max(max_pt, dfs(A))
        A.pop()
    return max_pt

ans = dfs([])
print(ans)
