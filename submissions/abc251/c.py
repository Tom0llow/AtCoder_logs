N = int(input())
S, T = set(), []
for _ in range(N):
    s, t = input().split()
    S_size = len(S)
    S.add(s)
    if S_size < len(S):
        T.append(int(t))
    else:
        T.append(0)

ans = T.index(max(T))+1
print(ans)
