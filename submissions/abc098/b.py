N = int(input())
A = list(map(int, input().split()))


res = 0
right = 0
sum_num = 0
# print(A)
for left in range(N):
    while right < N and sum_num^A[right] == sum_num+A[right]:
        sum_num += A[right]
        right += 1
        # print(A[left:right])
    res += right - left

    if left == right:    right += 1
    else:   sum_num -= A[left]

print(res)
