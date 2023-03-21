S = str(input())

from collections import defaultdict
d = defaultdict(int)
for s in S:
    d[s] += 1 
sorted_d = sorted(d.items())

ans = []
for s in sorted_d:
    ans.append(s[0]*s[1])
ans = ''.join(ans)
print(ans)
