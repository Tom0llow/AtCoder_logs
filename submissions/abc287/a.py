N = int(input())
cnt = 0
for _ in range(N):
    S = input()
    if S == 'For':
        cnt += 1

if cnt > N/2:
    print('Yes')
else:
    print('No')
