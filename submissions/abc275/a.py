N = int(input())
H = list(map(int,input().split()))

ans = 1+H.index(max(H))
print(ans)
