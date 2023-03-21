N, W = map(int, input().split())
A = list(map(int, input().split()))

cnt = set()
for i in range(N):
    n = A[i]
    if A[i] < W:
        cnt.add(n)
    for j in range(i+1, N):
        n = A[i]+A[j]
        if n <= W:
            cnt.add(n)
        for k in range(j+1, N):
            n = A[i]+A[j]+A[k]
            if n <= W:
                cnt.add(n)

print(len(cnt))
