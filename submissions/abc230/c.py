N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

ans = [['.'] * (S-R+1) for i in range(Q-P+1)]

k_min = max(max(1-A, 1-B), P-A, R-B)
k_max = min(min(N-A, N-B), Q-A, S-B)

for k in range(k_min, k_max+1):
    ans[A+k-P][B+k-R] = '#'

k_min = max(max(1-A, B-N), P-A, B-S)
k_max = min(min(N-A, B-1), Q-A, B-R)

for k in range(k_min, k_max+1):
    ans[A+k-P][B-k-R] = '#'

for i in ans:
    print(*i, sep='')
