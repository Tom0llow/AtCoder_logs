import itertools as it

N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]


num = list(range(1, N+1))
per_num = list(it.permutations(num))


ans = 0
for V in per_num:
    cnt = 0
    if V[0] == 1:
        for i in range(len(V)-1):
            E = sorted([V[i], V[i+1]])
            if E in ab:
                cnt += 1
        if cnt == N-1:
            ans += 1

print(ans)
