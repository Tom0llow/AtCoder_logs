N,K = map(int,input().split())
S = input()

nex = [[0 for _ in range(26)] for _ in range(N+1)]
for i in range(26):
    nex[N][i] = N
for i in range(N-1,-1,-1):
    for j in range(26):
        if ord(S[i])-ord('a') == j:
            nex[i][j] = i
        else:
            nex[i][j] = nex[i+1][j]

ans = ''
CurrentPos = 0
for i in range(1,K+1):
    for j in range(26):
        NexPos = nex[CurrentPos][j]
        MaxPossibleLength = (N-NexPos-1)+i
        if MaxPossibleLength >= K:
            ans += chr(ord('a')+j)
            CurrentPos = NexPos+1
            break

print(ans)
