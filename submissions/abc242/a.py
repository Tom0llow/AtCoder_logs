A, B, C, X = map(int, input().split())

if X <= A:
    ans = 1
elif B >= X >= A+1:
    ans = C / (B - A)
else:
    ans = 0

print(ans)
