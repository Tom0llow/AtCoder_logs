from itertools import product

N = int(input())

for pro in product([0,1],repeat=N):
    op = 0
    cl = 0
    for p in pro:
        if not p:   op += 1
        else: cl += 1

        if op < cl:
            break
        
    if op == cl:
        S = ''
        for p in pro: 
            S += '(' if not p else ')'
        print(S)
