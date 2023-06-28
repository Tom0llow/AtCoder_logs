N = int(input())
S = input()
T = input()

for i in range(N):
    if (S[i] == T[i]) or (S[i] in ['1','l'] and T[i] in ['1','l']) or (S[i] in ['0','o'] and T[i] in ['0','o']):
        continue
    else:
        print('No')
        exit()

print('Yes')
