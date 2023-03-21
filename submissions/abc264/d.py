S = input()
L = []
for s in S:
    if s == 'a':    n=1
    if s == 't':    n=2
    if s == 'c':    n=3
    if s == 'o':    n=4
    if s == 'd':    n=5
    if s == 'e':    n=6
    if s == 'r':    n=7
    L.append(n)

ans = 0
flag = True
for i in range(len(L)):
    if not flag:
        break
    flag = False
    for j in range(len(L)-i-1):
        if L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]
            flag = True
            ans += 1

print(ans)
