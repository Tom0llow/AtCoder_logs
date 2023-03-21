N,K = map(int,input().split())
A = list(map(int,input().split()))

A = set(sorted(A))
num = 0
for a in A:
    if (not num == a) or (K <= 0):
        break
    num += 1
    K -= 1

print(num)
