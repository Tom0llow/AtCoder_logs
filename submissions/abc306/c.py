from collections import defaultdict

N = int(input())
A = list(map(int,input().split()))

d = defaultdict(list)
for i in range(3*N):
    d[A[i]].append(i+1)

# print(d)

ans = [t[0] for t in sorted(d.items(), key=lambda x:(x[1][1]))]
print(*ans)
