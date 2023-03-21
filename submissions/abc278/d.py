from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))
Q = int(input())

diff = defaultdict(list)
add = 0
for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        diff = defaultdict(list)
        add = q[1]

    elif q[0] == 2:
        i,x = q[1],q[2]
        diff[i].append(x)
    else:
        i = q[1]
        if i in diff and add >= 1:
            print(sum(diff[i])+add)
        elif i in diff:
            print(A[i-1] + sum(diff[i])+add)
        elif add >= 1:
            print(add)
        else:
            print(A[i-1]+add)
