N,K = map(int,input().split())

if N == 0:
    print(0)
    exit()

def base_10(num_n,n):
    num_10 = 0
    for s in str(num_n):
        num_10 *= n
        num_10 += int(s)
    return num_10

def base_n(num_10,n):
    str_n = ''
    while num_10:
        if num_10%n >= 10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    return int(str_n[::-1])

def MtoN(num,m,n):
    num10 = base_10(num,m)
    return base_n(num10,n)

        
num = N
for _ in range(K):
    num = MtoN(num,8,9)
    num = int(str(num).replace('8','5'))

print(num)
