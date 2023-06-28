from collections import defaultdict


S = [s for s in input()]
T = [t for t in input()]


Sd = defaultdict(int)
Td = defaultdict(int)
N = len(S)
for i in range(N):
    Sd[S[i]] += 1
    Td[T[i]] += 1

    Sd[T[i]] += 0
    Td[S[i]] += 0


cntSat = 0
cntTat = 0
for s in Sd.keys():
    if s == '@':    continue
    if s != '@' and Sd[s] == Td[s]: continue

    if s not in ['a','t','c','o','d','e','r']:
        print('No')
        exit()

    if Sd[s] > Td[s]:   cntTat += Sd[s] - Td[s]
    else:   cntSat += Td[s] - Sd[s]

# print(cntSat,cntTat)
# print(Sd)
# print(Td)
if cntSat <= Sd['@'] and cntTat <= Td['@'] and Sd['@']-cntSat == Td['@']-cntTat:
    print('Yes')
else:
    print('No')
