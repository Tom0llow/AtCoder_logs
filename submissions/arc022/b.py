N = int(input())
A = list(map(int, input().split()))

res = 0
right = 0
tastes = set()
# print(A)

for left in range(N):
    while right < N and A[right] not in tastes:
        tastes.add(A[right]) 
        right += 1
        # print(A[left:right])

    res = max(res, right-left)

    if right == left:   right += 1 
    else:    tastes.remove(A[left])

print(res)
