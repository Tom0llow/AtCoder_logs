from collections import defaultdict
import sys

S = input()
S = '#'+S

if S[1] != '0':
    print('No')
    sys.exit()

pin = [[] for _ in range(7)]
for i in range(len(S)):
    if i == 7:
        pin[0].append(S[i])
    if i == 4:
        pin[1].append(S[i])
    if i == 2 or i == 8:
        pin[2].append(S[i])
    if i == 5 or i == 1:
        pin[3].append(S[i])
    if i == 3 or i == 9:
        pin[4].append(S[i])
    if i == 6:
        pin[5].append(S[i])
    if i == 10:
        pin[6].append(S[i])

for i in range(1,6):
    if '1' not in pin[i]:
        x = i
        flag = False
        while x <= 6:
            if '1' in pin[x]:
                flag = True
                break
            x += 1
        
        if flag:
            y = i
            flag = False
            while 0 <= y:
                if '1' in pin[y]:
                    flag = True
                    break
                y -= 1
        
        if flag:
            print('Yes') 
            sys.exit()

print('No')         
