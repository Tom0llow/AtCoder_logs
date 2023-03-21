from collections import defaultdict


N = int(input())
S = defaultdict(int)
for _ in range(N):
    s = input()
    S[s] += 1
    X = S[s]-1

    out = s
    if X > 0:   out = s+'({})'.format(X)
    print(out)
