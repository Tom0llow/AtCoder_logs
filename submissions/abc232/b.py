S = str(input())
T = str(input())
S_chr = []
T_chr = []

for i, j in zip(S, T):
    S_chr.append(ord(i) - ord('a'))
    T_chr.append(ord(j) - ord('a'))

ans = 'Yes'
a = (S_chr[0] - T_chr[0]) % 26
for i, j in zip(S_chr, T_chr):
    if (i - j) % 26 != a:
        ans = 'No'
        break

print(ans)
