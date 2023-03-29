from collections import defaultdict

N,M = map(int,input().split())
E = defaultdict(list)
for _ in range(M):
    a,b = map(int,input().split())
    E[a-1].append(b-1)
    E[b-1].append(a-1)

for e in E[0]:
    for j in E[e]:
        if j==N-1:
            print('POSSIBLE')
            exit()
print('IMPOSSIBLE')
        
