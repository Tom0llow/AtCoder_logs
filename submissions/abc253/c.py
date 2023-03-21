from collections import defaultdict
 
Q = int(input())
S = defaultdict(int)

min_v = 10**10
max_v = -1

for _ in range(Q):
    q = list(map(int, input().split()))
    
    if q[0] == 1:
        x = q[1]
        S[x] += 1
        min_v = min(min_v, x)
        max_v = max(max_v, x)
    
    elif q[0] == 2:
        x = q[1]
        S[x] -= min(q[2], S[x])
        if S[x] == 0:    
            del S[x]
            if S:
                if x == min_v:
                    min_v = min(S)
                if x == max_v:
                    max_v = max(S)
            else:
                min_v = 10**10
                max_v = -1

    else:
        print(max_v-min_v)
