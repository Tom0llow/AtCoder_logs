N = int(input())
class1 = [0]*(N+1)
class2 = [0]*(N+1)
for i in range(N):
    C,P = map(int,input().split())
    if C == 1:  class1[i+1] = P
    else:   class2[i+1] = P

for i in range(1,N+1):
    class1[i] += class1[i-1]
    class2[i] += class2[i-1]

# print(class1)
# print(class2)

Q = int(input())
for _ in range(Q):
    L,R = map(int,input().split())

    ans1 = class1[R] - class1[L-1]
    ans2 = class2[R] - class2[L-1]
    print(ans1, ans2)
