N, L, W = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
right = 0
for x in a:
    if right < x:
        len = x - right
        ans += (len + W - 1) // W
    right = x + W

if right < L:
    len = L - right
    ans += (len + W - 1) // W

print(ans)
