N = int(input())
S = str(input())

ans = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            if str(i) in S:
                a = S[S.index(str(i))+1:]
                if str(j) in a:
                    b = a[a.index(str(j))+1:]
                    if str(k) in b:
                        ans += 1
                    
print(ans)
