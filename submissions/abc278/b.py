H,M = map(int,input().split())

H = str(H) if len(str(H)) == 2 else '0'+str(H)
M = str(M) if len(str(M)) == 2 else '0'+str(M)

A,B = H[0],H[1]
C,D = M[0],M[1]

while True:
    h,m = int(A+C),int(B+D)
    if 0<=h<=23 and 0<=m<=59:
        print(A+B,C+D)
        break
    
    if int(C+D)+1 <= 59:
        C = str(int(C+D)+1)[0]
        D = str(int(C+D)+1)[1]
    else:
        C = '0'
        D = '0'
        if int(A+B)+1 <= 23:
            A = str(int(A+B)+1)[0]
            B = str(int(A+B)+1)[1]
        else:
            A = '0'
            B = '0'
