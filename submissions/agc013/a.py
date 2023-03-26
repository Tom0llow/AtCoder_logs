N = int(input())
A = list(map(int,input().split()))

ans = 1
temp = 0
for i in range(N-1):
    if temp == 0:
        if A[i] < A[i+1]:
            temp += 1
        elif A[i] > A[i+1]:
            temp -= 1
    elif temp > 0:
        if A[i] > A[i+1]:
            ans += 1
            temp = 0
    else:
        if A[i] < A[i+1]:
            ans += 1
            temp = 0

print(ans)
