import math

a, b, d = map(int, input().split())

theta = d * (math.pi/180)
x, y = math.cos(theta)*a - math.sin(theta)*b, math.sin(theta)*a + math.cos(theta)*b, 

print(x, y)
