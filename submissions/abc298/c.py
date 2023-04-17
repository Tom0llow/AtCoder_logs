from collections import defaultdict

N = int(input())
Q = int(input())

box = defaultdict(list)
card = defaultdict(set)

for _ in range(Q):
    query = list(map(int,input().split()))
    
    if query[0] == 1:
        i,j = query[1:]
        box[j].append(i)
        card[i].add(j)

    elif query[0] == 2:
        i = query[1]
        print(*sorted(box[i]))
    
    else:
        i = query[1]
        print(*sorted(list(card[i])))
