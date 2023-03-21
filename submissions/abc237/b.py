import numpy as np

H, W = map(int, input().split())
A = [0]*H
for i in range(H):
    A[i] = list(map(int, input().split()))

B = np.transpose(A)
    
for i in range(W):
    ans = ' '.join(map(str, B[i])) 
    print(ans)
