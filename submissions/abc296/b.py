S = ['']*8
for i in range(8):
    S[i] = input()

cnt = 8
for s in S:
    for i in range(8):
        if s[i] == '*':
            ans = chr(ord('a')+i) + str(cnt)
            print(ans)
            exit()
    cnt -= 1
