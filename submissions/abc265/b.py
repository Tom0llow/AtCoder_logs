from collections import defaultdict


N, M, T = map(int, input().split())

A = list(map(int, input().split()))
cost = defaultdict(list)
for i in range(N-1):
    cost[i+2].append(A[i])
    cost[i+2].append(0)

for _ in range(M):
    X, Y = map(int,input().split())
    cost[X][1] = Y 


ans = 'Yes'
for i in range(N-1):
    T -= cost[i+2][0]
    if T <= 0:
        ans = 'No'
        break
    T += cost[i+2][1]

print(ans)
