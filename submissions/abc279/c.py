from collections import defaultdict


H,W = map(int,input().split())

S = defaultdict(list)
for _ in range(H):
    s = input()
    for v in range(W):
        S[v].append(s[v])

T = defaultdict(list)
for _ in range(H):
    t = input()
    for v in range(W):
        T[v].append(t[v])


S_list =  sorted(list(S.values()))
T_list =  sorted(list(T.values()))

ans = 'No'
if S_list == T_list:
    ans = 'Yes'
print(ans)
