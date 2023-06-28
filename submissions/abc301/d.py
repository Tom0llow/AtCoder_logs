S = input()
N = int(input())


n = 0
while True:
    if N == pow(2,n):   break
    elif N < pow(2,n):
        n -= 1
        break

    n += 1

# print(n)
# print(S[n:])
ans = 0
for i in range(len(S)):
    x = len(S)-(i+1)
    ans += pow(2,x) if S[i] == '1' else 0

for i in range(len(S)):
    x = len(S)-(i+1)
    if x <= n:
        if S[i] == '?':
            if ans+pow(2,x) <= N:
                ans += pow(2,x)

ans = ans if ans <= N else -1
print(ans)
