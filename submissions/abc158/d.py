from collections import deque

S = input()
deq = deque()
for s in S:
    deq.append(s)

Q = int(input())
isRev = False
for _ in range(Q):
    query = input().split()

    if query[0] == '1':
        isRev = not isRev
    else:
        f = query[1]
        c = query[2]
        if f == '1':
            if isRev:   deq.append(c)
            else:   deq.appendleft(c)
        else:
            if isRev:   deq.appendleft(c)
            else:   deq.append(c)

ans = ''
if isRev:
    while deq:
        ans += deq.pop()
else:
    while deq:
        ans += deq.popleft()

print(ans)
