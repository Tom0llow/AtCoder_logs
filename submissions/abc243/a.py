V, A, B, C = map(int, input().split())

R = V % (A+B+C)
if R >= A:
    R -= A
    if R >= B:
        ans = 'T'
    else:
        ans = 'M'
else:
    ans = 'F'

print(ans)
