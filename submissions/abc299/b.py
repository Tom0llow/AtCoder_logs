from collections import defaultdict


N,T = map(int,input().split())
C = list(map(int,input().split()))
R = list(map(int,input().split()))

r0 = -1
r1 = R[0]
for i in range(N):
    if C[i] == T:
        if r0 <= R[i]:
            r0 = R[i]
            ans0 = i+1

    if C[i] == C[0]:
        if r1 <= R[i]:
            r1 = R[i]
            ans1 = i+1


if r0 != -1:    
    print(ans0)
else:
    print(ans1)
    
