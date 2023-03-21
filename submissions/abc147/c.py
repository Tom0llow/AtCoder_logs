from itertools import product

N = int(input())
A = []
for _ in range(N):
    n = int(input())
    A.append([[*map(int, input().split())] for _ in range(n)])

ans = 0
for bit in product([0,1], repeat=N):
    flag = True
    for j in range(N):
        if bit[j]:
            for k in A[j]:
                if not bit[k[0]-1] == k[1]:
                    flag = False
                    break
            if not flag:
                break
    if flag: ans = max(ans, sum(bit))
print(ans)
