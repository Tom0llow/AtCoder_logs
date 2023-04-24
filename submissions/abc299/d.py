N = int(input())

l,r = 1,N
m = (l+r) // 2
while True:
    if l+1 == r:
        print('! '+str(l))
        exit()
    
    print('? '+str(m))
    si = int(input())

    if si == 0: l,r = m,r
    else:   l,r = l,m

    m = (l+r) // 2



    
