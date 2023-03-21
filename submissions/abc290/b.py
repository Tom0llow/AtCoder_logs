N,K = map(int,input().split())
S = input()

ans = ''
for i in range(N):
    if K <= 0:
        ans += 'x'*(N-i)
        break

    if S[i] == 'o':
        ans += 'o'
        K -= 1
    else:
        ans += 'x'


print(ans)
