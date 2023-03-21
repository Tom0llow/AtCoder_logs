N = int(input())
P = list(map(int,input().split()))

j = N-2
while P[j] < P[j+1]:
    j -= 1

k = N-1
while P[j] < P[k]:
    k -= 1

# print(j,k)

P[j],P[k] = P[k],P[j]
print(*P[:j+1], *P[:j:-1])
