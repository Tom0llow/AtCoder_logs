N,Q = map(int,input().split())
A = list(map(int,input().split()))

def shift(a,cnt):
    if cnt == 0:    return a
    return a-cnt if a > cnt else a+(N-cnt)

cnt = 0
for _ in range(Q):
    T,x,y = map(int,input().split())
    x, y = shift(x,cnt)-1, shift(y,cnt)-1    

    # print(x,y)    
    if T == 1:
        A[x],A[y] = A[y],A[x]

    elif T == 2:
        cnt += 1

    elif T == 3:
        print(A[x])

    if cnt == N:    cnt = 0
