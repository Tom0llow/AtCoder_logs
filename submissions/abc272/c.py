N = int(input())
A = list(map(int,input().split()))

odd = []
even = []

for i in range(N):
    if A[i]%2 == 0: even.append(A[i])
    else:   odd.append(A[i])

odd.sort()
even.sort()

a = sum(odd[-2:]) if len(odd) >= 2 else -1
b = sum(even[-2:]) if len(even) >= 2 else -1

print(max(a,b))
