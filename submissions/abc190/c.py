#product
from itertools import product 
from collections import Counter

N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(M)]
K = int(input())
CD = [tuple(map(int, input().split())) for _ in range(K)]

def calc(pro):
    counter = Counter()
    for i in range(K):
        choice = CD[i][pro[i]]
        counter[choice] += 1
    
    ret = 0
    for a, b in AB:
        if counter[a] > 0 and counter[b] > 0:
            ret += 1
    return ret

ans = 0
for pro in product([0,1], repeat=K):
    ans = max(ans, calc(pro))
print(ans)
