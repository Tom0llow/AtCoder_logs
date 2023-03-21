from itertools import product

N, M, X = map(int, input().split())
C = []
A = []
for _ in range(N):
    CA = list(map(int, input().split()))
    C.append(CA[0])
    A.append(CA[1:])

def solve(pro):
    SUM = 0
    finished = []
    for i in range(N):
        if pro[i]:
            SUM += C[i]
            finished.append(A[i])
    finished = [sum(column) for column in zip(*finished)]    
    cnt = 0
    for f in finished:
        if f >= X:  cnt += 1
    if cnt == len(finished):    return SUM

ans = []
for pro in product((0, 1), repeat=N):
    if solve(pro) != None:
        ans.append(solve(pro))
ans = sorted(ans)
if len(ans) != 1:   print(ans[1])
else:   print(-1)
