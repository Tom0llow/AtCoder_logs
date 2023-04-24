from collections import defaultdict

N = int(input())
S = input()

A = [s for s in S]

d = defaultdict(int)
ans = 0
right = 0
for left in range(0,N-1):

    while (right < N) and (d['o'] < 1 or d['x'] < 1):    
        d[A[right]] += 1
        right += 1

    # print(d, left, right-1)
    if d['o'] >= 1 and d['x'] >= 1: ans += N - (right-1)
    
    if right == left: right += 1
    else: d[A[left]] -= 1

print(ans)
