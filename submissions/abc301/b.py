N = int(input())
A = list(map(int,input().split()))


cnt = 0
ans = A.copy()
for i in range(N-1):
    if abs(A[i]-A[i+1]) != 1:
        if A[i] < A[i+1]:
            a = list(range(A[i]+1,A[i+1]))
        
        else:
            a = list(range(A[i]-1,A[i+1],-1))
        
        ans[i+1+cnt:i+1+cnt] = a
        cnt += len(a)

print(*ans)
