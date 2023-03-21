from collections import defaultdict
from itertools import product

N, M = map(int, input().split())
k = []
switches = []
for _ in range(M):
    ks = list(map(int, input().split()))
    k.append(ks[0])
    switches.append(ks[1:])
p = list(map(int, input().split()))


def solve(pro):
    on_switches = []
    for i in range(N):
        if pro[i]:
            on_switches.append(i+1)
    
    check_swithces = defaultdict(int)
    for j in range(M):    
        check_swithces[j+1] = 0
        for s in switches[j]:
            if s in on_switches:
                check_swithces[j+1] += 1

    cnt = 0
    for j in range(M):
        if p[j] == check_swithces[j+1] % 2:
            cnt += 1
    return 1 if cnt == len(check_swithces) else 0   


ans = 0
for pro in product((0,1), repeat=N):
    ans += solve(pro)
print(ans)


