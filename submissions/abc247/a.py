S = input()
ans = '0'
for s in S:
    if s == '1':
        ans += '1'
    else:
        ans += '0'

print(ans[:-1])
