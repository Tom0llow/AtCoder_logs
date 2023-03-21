from itertools import product
import sys

H1, W1 = map(int, input().split())
A = []
for _ in range(H1):
    a = list(map(int, input().split()))
    A.append(a)
H2, W2 = map(int, input().split())
B = []
for _ in range(H2):
    b = list(map(int, input().split()))
    B.append(b)

for pro1 in product([0,1], repeat=H1):
    for pro2 in product([0,1], repeat=W1):
        
        h, w = [], []
        for i in range(H1): 
           if pro1[i]: h.append(i)
        for j in range(W1):
           if pro2[j]: w.append(j)   
        if len(h) != H2 or len(w) != W2:    continue

        flag = True
        for k in range(H2):
            for l in range(W2):
                if A[h[k]][w[l]] != B[k][l]:
                    flag = False
                    break
        
        if flag:    
            print('Yes')
            sys.exit()

print('No')

