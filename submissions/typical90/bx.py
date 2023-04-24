N = int(input())
A = list(map(int,input().split()))

whole = sum(A)
A += A
# print(A)

cnt = 0
right = 0
for left in range(0,2*N):
    while (right < 2*N) and (right-left < N) and (cnt <= whole/10):
        cnt += A[right]
        right += 1

        if cnt == whole/10:
            print('Yes')
            exit()

    if right == left: right += 1
    else: cnt -= A[left]

print('No')
