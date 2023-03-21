L, R = map(int, input().split())
S = input()

s = S[L-1:R]
ans = S[:L-1] + s[::-1] + S[R:]

print(ans)
