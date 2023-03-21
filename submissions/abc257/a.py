N, X = map(int, input().split())
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans = ''
for i in range(len(alphabet)):
    ans += alphabet[i]*N

print(ans[X-1])
