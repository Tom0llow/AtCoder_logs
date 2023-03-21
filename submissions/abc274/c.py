N = int(input())
A = list(map(int,input().split()))
A = [0]+A
# [1,2,2,3,3,4,4,3,3]

ame = [0 for _ in range(2*N+2)]
for i in range(1,N+1):
    ame[2*i] = ame[A[i]]+1
    ame[2*i+1] = ame[A[i]]+1
     
for k in range(1,2*N+2):
    print(ame[k])
