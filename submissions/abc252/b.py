N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 'No'
most_delicious = max(A)
for i in range(K):
    if A[B[i]-1] == most_delicious:
        ans = 'Yes'

print(ans)
