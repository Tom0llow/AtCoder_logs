import bisect

N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

C = sorted(A+B)

ansA = []
for a in A:
    ansA.append(bisect.bisect_left(C,a)+1)

ansB = []
for b in B:
    ansB.append(bisect.bisect_left(C,b)+1)


print(*ansA)
print(*ansB)
