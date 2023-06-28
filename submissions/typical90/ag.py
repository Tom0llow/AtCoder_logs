H,W = map(int,input().split())

ans = -(-H//2) * -(-W//2) if H != 1 and W != 1 else H*W
print(ans)
