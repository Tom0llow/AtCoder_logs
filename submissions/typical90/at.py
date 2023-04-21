from collections import defaultdict

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

dA = defaultdict(int)
dB = defaultdict(int)
dC = defaultdict(int)

for i in range(N):
    dA[A[i]%46] += 1
    dB[B[i]%46] += 1
    dC[C[i]%46] += 1

# print(dA)
# print(dB)
# print(dC)

ans = 0
for x in range(46):
    for y in range(46):
        for z in range(46): 
            if (x+y+z) % 46 == 0:
                ans += dA[x]*dB[y]*dC[z]
            
print(ans)
