N,L = map(int,input().split())
K = int(input())
A = list(map(int,input().split()))

Y = [A[0]] + [A[i+1]-A[i] for i in range(N-1)] + [L-A[-1]]
# print(Y)

left = 0
right = L
while right-left > 1:
    M = (left+right) // 2

    cnt = 0
    length = 0
    for i in range(N+1):
        length += Y[i]

        if cnt < K and length >= M:
            cnt += 1
            length = 0

    if length >= M: left,right = M,right 
    else:   left,right = left,M
        

print(left)
        
