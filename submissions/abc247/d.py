from collections import deque


def judge(c, xc, cnt):
    x, c2 = xc[0], xc[1]

    if c < c2:
        c2 -= c
        cnt += x * c
        dq.appendleft([x, c2])
    
    elif c == c2:
        cnt += x * c
    
    else:
        cnt += x * c2
        c -= c2
        xc = dq.popleft()
        cnt = judge(c, xc, cnt)

    return cnt 



Q = int(input())
dq = deque()
for _ in range(Q):
    query = input().split()
    if query[0] == '1':
        x, c = int(query[1]), int(query[2])
        dq.append([x, c])

    else:
        c = int(query[1])
        xc = dq.popleft()
        
        cnt = judge(c, xc, 0)          
        print(cnt)
   
