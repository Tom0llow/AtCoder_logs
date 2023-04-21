import math

A,B = map(int,input().split())

def my_lcm(x,y):
    return (x*y) // math.gcd(x,y)

ans = my_lcm(A,B)
if ans > pow(10,18):    ans = 'Large' 
print(ans)
