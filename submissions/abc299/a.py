N = int(input())
S = input()


ind0 = []
ind1 = []
for i in range(N):
    if S[i] == '|':
        ind0.append(i)
    if S[i] == '*':
        ind1.append(i)

if ind0[0] < ind1[0] < ind0[1]:
    print('in')
else:
    print('out')
