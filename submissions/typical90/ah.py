from collections import defaultdict

N,K = map(int,input().split())
a = list(map(int,input().split()))

ans = 0
right = 0
d = defaultdict(int)
for left in range(0,N):

    while right < N:
        d[a[right]] += 1
        right += 1

        if len(d) > K:
            right -= 1
            d[a[right]] -= 1
            break

    ans = max(ans, right-left)
    # print(d, a[left:right])

    if right == left:   right += 1
    else:   
        d[a[left]] -= 1
        if d[a[left]] == 0:
            d.pop(a[left])

print(ans)
    
