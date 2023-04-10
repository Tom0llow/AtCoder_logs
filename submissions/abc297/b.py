import re

S = input()

Bx,By =  [m.span() for m in re.finditer('B', S)]
Rx,Ry =  [m.span() for m in re.finditer('R', S)]
Kz = re.search('K', S).span()


if (Bx[1]%2 != By[1]%2) and (Rx[1] < Kz[1] < Ry[1]):
    print('Yes')
    exit()

print('No')
