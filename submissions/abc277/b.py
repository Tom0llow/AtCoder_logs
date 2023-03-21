N = int(input())
S = set()
for _ in range(N):
    s = input()
    if s[0] in ['H','D','C','S'] and s[1] in ['A','2','3','4','5','6','7','8','9','T','J','Q','K']:
        S.add(s)

ans = 'No'
if len(S) == N:
    ans = 'Yes'
print(ans)
