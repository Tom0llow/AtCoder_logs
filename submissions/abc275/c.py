def dist(A,B):
    x,y = A[0],A[1]
    u,v = B[0],B[1]
    return (x-u)**2+(y-v)**2

S = [input() for _ in range(9)]

cods = []
for y in range(9):
    for x in range(9):
        if S[y][x] == '#':
            cods.append((y+1,x+1))

cnt = 0
N = len(cods)
for i in range(N-3):
    A = cods[i]
    for j in range(i+1,N-2):    
        B = cods[j]
        for k in range(j+1,N-1):
            C = cods[k]
            for l in range(k+1,N):
                D = cods[l]

                ab = dist(A,B)
                ac = dist(A,C)
                ad = dist(A,D)
                bc = dist(B,C)
                bd = dist(B,D)
                cd = dist(C,D)

                edges = [ab,ac,ad,bc,bd,cd]
                if len(set(edges)) == 2:
                    cnt += 1

print(cnt)
                
