N,Q = map(int,input().split())
A = list(map(int,input().split()))

B = [0]*(N)
ans = 0
for i in range(N-1):
    B[i] = A[i+1]-A[i]
    ans += abs(B[i])

# print(B)
for _ in range(Q):
    L,R,V = map(int,input().split())

    mae = abs(B[(L-1)-1])+abs(B[R-1])

    if L >= 2:  B[(L-1)-1] += V
    if R <= N-1:    B[R-1] -= V

    ato = abs(B[(L-1)-1])+abs(B[R-1])

    ans += (ato - mae)

    print(ans)
