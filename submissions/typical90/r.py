import math


T = int(input())
L,X,Y = map(int,input().split())
Q = int(input())
E = [int(input()) for _ in range(Q)]


for e in E:
    t = math.radians((e/T-1/4)*360)

    x = 0
    y = -L/2 * math.cos(t)
    z = L/2 * (1 + math.sin(t))
    
    d = math.sqrt((X-x)**2 + (Y-y)**2)
    h = z
  
    ans = 90 - math.degrees(math.atan2(d, h)) if h != 0 else 0
    print(ans)
