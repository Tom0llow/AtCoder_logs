W = int(input())

A = []
for i in range(1,100):
    A.append(i)
    
for i in range(100, 10000, 100):
    A.append(i)

for i in range(10000, 1000001, 10000):
    A.append(i)

print(len(A))
print(*A)

