import itertools

N = int(input())
class1 = [0]*N
class2 = [0]*N
for i in range(N):
    C,P = map(int,input().split())
    if C == 1:  class1[i] = P
    else:   class2[i] = P

t1 = [0]+list(itertools.accumulate(class1))
t2 = [0]+list(itertools.accumulate(class2))


Q = int(input())
for _ in range(Q):
    L,R = map(int,input().split())
    A = t1[R] - t1[L-1] if len(t1) >= 2 else t1[0]
    B = t2[R] - t2[L-1] if len(t2) >= 2 else t2[0]
    print(A,B)

