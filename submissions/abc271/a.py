N = int(input())

ans = hex(N)
if N <= 15:
    ans = '0'+str.upper(ans[2:])
else:
    ans = str.upper(ans[2:])
    
print(ans)
