S = input()

N = len(S)
ans = 1
for i in range(1,N):
    ans += 26**i

for s in S:
    n = ord(s)-64
    ans += (n-1) * 26**(N-1)
    N -= 1

print(ans)
