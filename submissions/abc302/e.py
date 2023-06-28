from collections import defaultdict


N,Q = map(int,input().split())
Query = [list(map(int,input().split())) for _ in range(Q)]


ans = N
e = defaultdict(set)
for q in Query:
    if q[0] == 1:
        u,v = q[1:]
        if len(e[u]) == 0:    ans -= 1
        if len(e[v]) == 0:    ans -= 1

        e[u].add(v)
        e[v].add(u)

    else:
        u = q[1]
        for v in e[u]:
            e[v].remove(u)
            if len(e[v]) == 0:  ans += 1

        if len(e[u]) > 0:   ans += 1
        e[u].clear()

    print(ans)
