import functools
import math


def my_lcm_base(x,y):
    return (x*y) // math.gcd(x,y)

def my_lcm(*intergers):
    return functools.reduce(my_lcm_base, intergers)


A,B = map(int,input().split())

lcm = my_lcm(A,B)
ans = lcm if lcm <= pow(10,18) else 'Large'
print(ans)
