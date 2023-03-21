S = list(input() for _ in range(10))

cnt = 0
A = 0
for i in range(10):
    for j in range(10):
        if S[i][j] == '#':
            if cnt == 0:
                A = i+1
                C = j+1
            cnt += 1
    if A: break

D = C+cnt-1

for i in range(1,11):
    if '#' in S[-i]:
        B = 10-i+1
        break

print(A,B)
print(C,D)
