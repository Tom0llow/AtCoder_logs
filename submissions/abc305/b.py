from collections import defaultdict


p,q = input().split()

dist = defaultdict(int)
dist['AB'] = 3
dist['BC'] = 1
dist['CD'] = 4
dist['DE'] = 1
dist['EF'] = 5
dist['FG'] = 9


for s1 in 'ABCDEFG':
    for s2 in 'ABCDEFG':
        if s1 == s2:    continue
        if dist[s1+s2] > 0: continue
        if s1 > s2:
            dist[s1+s2] = dist[s2+s1]

        tmp = s1
        for s in 'ABCDEFG':
            if s <= s1:  continue
            if s > s2:  break
            dist[s1+s2] += dist[tmp+s]
            tmp = s

# print(dist)
print(dist[p+q])
