x = list(map(int, list(input())))
n = len(x)
cnt = [0]*(n+1)

for i in range(n):
    cnt[i+1] = cnt[i] + x[i]
pre = 0
ans = ''
for i in range(n):
    d = cnt[n-i] + pre
    if len(str(d)) >= 2:
        pre = int(str(d)[:-1])
    else:
        pre = 0
    ans += str(d)[-1]

if pre != 0:
    ans += str(pre)
print(ans[::-1])
