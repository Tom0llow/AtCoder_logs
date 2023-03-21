A, B, C, D = map(int, input().split())

if A == C:
    if B <= D:
        ans = 'Takahashi'
    else:
        ans = 'Aoki'
elif A < C:
    ans = 'Takahashi'
else:
    ans = 'Aoki'

print(ans)
