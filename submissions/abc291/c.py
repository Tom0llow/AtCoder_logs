N = int(input())
S = input()

visited = []
x,y = (0,0)
visited.append((x,y))

for s in S:
    if s == 'R':
        x,y = (x+1,y)
    elif s == 'L':
        x,y = (x-1,y)
    elif s == 'U':
        x,y = (x,y+1)
    elif s == 'D':
        x,y = (x,y-1)

    visited.append((x,y))


ans = 'No'
if len(set(visited)) < len(visited):
    ans = 'Yes'

print(ans)
