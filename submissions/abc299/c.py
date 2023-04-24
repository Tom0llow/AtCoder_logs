N = int(input())
S = input()


f = 0
if S[0] == '-':
    cnt = 0
    flag = False
    f = 1
else:
    cnt = 1
    flag = True

ans = -1
for i in range(1,N):
    if S[i] == 'o':
        if flag:    
            cnt += 1
        else:   
            cnt = 1
            flag = True
        if i == N-1 and f:
            ans = max(ans,cnt)

    elif S[i] == '-':
        f = 1
        if flag:    
            ans = max(ans,cnt)
            flag = False
            cnt = 0

        
print(ans)
            
