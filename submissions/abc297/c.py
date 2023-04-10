H,W = map(int,input().split())

ans = []
for _ in range(H):
    S = input()
    S = S.replace('TT','PC')
    ans.append(S)

print(*ans, sep='\n')



