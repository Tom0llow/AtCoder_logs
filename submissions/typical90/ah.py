from collections import defaultdict


N,K = map(int,input().split())
a = list(map(int,input().split()))

num_counter = defaultdict(int)
cnt = 0
ans = 0
right = 0
for left in range(0,N):
    while (right < N):
        num_counter[a[right]] += 1

        if len(num_counter) > K:
            num_counter.pop(a[right])
            break

        right += 1

    ans = max(ans, (right - left))
    
    if right == left: right += 1
    else:             num_counter[a[left]] -= 1
    
    if num_counter[a[left]] == 0:
        num_counter.pop(a[left])

print(ans)
