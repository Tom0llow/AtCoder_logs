N,X,Y = map(int,input().split())
A = list(map(int,input().split()))

Ax = A[::2]
Ay = A[1::2]
Nx = (N+1)//2
Ny = N-Nx

DPx = [set() for _ in range(Nx+1)]
DPy = [set() for _ in range(Ny+1)]
DPx[1].add(Ax[0])
DPy[0].add(0)

for i in range(1,Nx):
    for x in DPx[i]:
        DPx[i+1].add(x+Ax[i])
        DPx[i+1].add(x-Ax[i])

for i in range(Ny):
    for y in DPy[i]:
        DPy[i+1].add(y+Ay[i])
        DPy[i+1].add(y-Ay[i])

if X in DPx[Nx] and Y in DPy[Ny]:
    print('Yes')
else:
    print('No')
