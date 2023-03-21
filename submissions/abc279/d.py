import math
A,B = map(int,input().split())

# f(x) = Bx + A/sqrt(x+1)
# f'(x) = B + (-A/2)*(1/(x+1)^(3/2)) 
# B + (-A/2)*(1/(x+1)^(3/2)) = 0
# x = (A/2B)^(2/3) - 1

def f(x):
    return B*x + A/math.sqrt(x+1)

x = (A/(2*B))**(2/3)-1
l = max(x-5,0)
r = min(x+5,A/B)
ans = A
for i in range(int(l),int(r)+1):
    ans = min(ans,f(i))

print(ans)
