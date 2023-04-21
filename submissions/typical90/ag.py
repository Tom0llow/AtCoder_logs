H,W = map(int,input().split())

if H == 1 or W == 1:
    print(H*W)
    exit()

H = H+1 if H%2 != 0 else H
W = W+1 if W%2 != 0 else W
print(H*W // 4)
