import math
import functools

A,B,C = map(int,input().split())

def my_gcd(*integers):
    return functools.reduce(math.gcd, integers)

mgcd = my_gcd(A,B,C)
ans = (A//mgcd)-1 + (B//mgcd)-1 + (C//mgcd)-1
print(ans)
