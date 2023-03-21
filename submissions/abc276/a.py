S = input()

ans = -1
S = S[::-1]
for i in range(len(S)):
    if S[i] == 'a':
        ans = len(S)-i 
        break
print(ans)
