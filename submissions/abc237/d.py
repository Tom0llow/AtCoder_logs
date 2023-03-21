L = []
R = []
N = int(input())
S = str(input())

for i, c in enumerate(S):
    if c == 'L': R.append(i)
    else: L.append(i)

ans = L + [N] + R[::-1]
print(*ans)
