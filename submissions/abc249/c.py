from itertools import product
from collections import defaultdict

def judge(pro):
    S = ''
    for i in range(N):
        if pro[i]:
            S += S_list[i]

    # print(S)
    c_dict = defaultdict(int)
    for c in S:
        c_dict[c] += 1
    
    # print(c_dict)
    cnt = 0
    for v in c_dict.values():
        if v == K:  cnt += 1
    
    return cnt



N, K = map(int, input().split())
S_list = [input() for _ in range(N)]


ans = 0
for pro in product((0,1), repeat=N):
    # print(pro)
    ans = max(judge(pro), ans)

print(ans)
