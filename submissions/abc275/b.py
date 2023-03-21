A,B,C,D,E,F = map(int,input().split())

x = (A*B*C)-(D*E*F)
ans = x%998244353
print(ans)
