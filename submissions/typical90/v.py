import functools
import math


def my_gcd(*intergers):
    return functools.reduce(math.gcd, intergers)

A,B,C = map(int,input().split())
x = my_gcd(A,B,C)

ans = (A//x-1) + (B//x-1) + (C//x-1)
print(ans)
