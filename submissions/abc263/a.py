from collections import defaultdict

cards = list(map(int, input().split()))
d = defaultdict(int)

for card in cards:
    d[card] += 1 

ans = 'No'
if len(d) == 2:
    flag = True
    for v in d.values():
        if not (v == 2 or v == 3):
            flag = False
            break
    if flag:
        ans = 'Yes'

print(ans)
