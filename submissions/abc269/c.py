from itertools import product

N = int(input())
b = bin(N)

x = []
for i in range(1,len(b)+1):
    if b[-i] == '1':
        k = int(i)-1
        x.append(2**k)

ans = []
for pro in product([0,1], repeat=len(x)):
    res = 0
    for i in range(len(x)):
        if pro[i]:
            res += x[i]
    ans.append(res)

ans = sorted(ans)
print(*ans, sep='\n')
