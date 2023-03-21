X,Y,Z = map(int,input().split())
# X:Goal, Y:Wall, Z:Hammer

if (0<Y<X<Z) or (0<Y<Z<X) or (Z<X<Y<0) or (X<Z<Y<0):
    ans = -1
elif  (Z<0<Y<X) or (X<Y<0<Z):
    ans = abs(X)+abs(Z)*2
else:
    ans = abs(X)
    # if (0<Z<Y<X) or (X<Y<Z<0) or (0<X<Y<Z) or (Z<Y<X<0) or (0<X<Z<Y) or (Y<Z<X<0) or (Z<Y<0<X) or (X<0<Y<Z) or (Y<Z<0<X) or (X<0<Z<Y) or (Y<0<Z<X) or (X<Z<0<Y) or (Y<0<X<Z) or (Z<X<0<Y):
    #     ans = abs(X)
    
print(ans)

