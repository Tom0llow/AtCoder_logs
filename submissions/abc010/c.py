import math

sx,sy,gx,gy,T,V = map(int,input().split())
n = int(input())
ans = 'NO'
for _ in range(n):
    x,y = map(int,input().split())

    dist1 = math.sqrt((x-sx)**2+(y-sy)**2)
    dist2 = math.sqrt((gx-x)**2+(gy-y)**2)

    if dist1+dist2 <= T*V:
        ans = 'YES'

print(ans)
        
