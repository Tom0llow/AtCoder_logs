from itertools import product


N,M = map(int,input().split())
S = []
for _ in range(M):
    C = int(input())
    S.append(list(map(int,input().split())))


x = [v for v in range(1,N+1)]

def judge(pro):
    s = []
    for i in range(M):
        if pro[i]:
            s += S[i]

    return 1 if list(set(s)) == x else 0
    

ans = 0
for pro in product((0,1), repeat=M):
    ans += judge(pro)

print(ans)
