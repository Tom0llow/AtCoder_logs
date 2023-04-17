import math

T = int(input())
L,X,Y = map(int,input().split())
Q = int(input())
E = list(int(input()) for _ in range(Q))

for e in E:
    rad = math.radians((e/T)*360-90)

    x = 0
    y = L/2 * (-math.cos(rad))
    z = L/2 * (1+math.sin(rad))

    # print(x,y,z)

    d = math.sqrt((X-x)**2 + (Y-y)**2)
    h = z    
    theta = math.atan2(h,d)
    ans = math.degrees(theta) 
    print(ans)
