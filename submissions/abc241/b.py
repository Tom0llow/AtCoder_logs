N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 'Yes'
for i in range(M):
    if not B[i] in A:
        ans = 'No'
        break
    else:
        A.remove(B[i])
print(ans)
