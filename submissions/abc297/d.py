A,B  = map(int,input().split())

cnt = 0

while A != B:
    if A < B:   A,B = B,A
    if A % B == 0:
        cnt += A//B-1
        break
    Q = A//B
    A = A-B*Q
    cnt += Q

print(cnt)

