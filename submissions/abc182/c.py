from itertools import product

N = str(input())

INF = 1 << 60
def solve(pro):
    judge = ''
    for i in range(len(N)):
        if pro[i]:
            judge += N[i]
    if not judge:   return INF
    if int(judge) % 3 == 0: return pro.count(0)
    else:   return INF

ans = INF
for pro in product((0,1), repeat=len(N)):
    ans = min(ans, solve(pro))

print(ans if ans != INF else -1)
