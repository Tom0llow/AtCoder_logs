N = int(input())
A = list(map(int,input().split()))


B = []
day = 0
cnt = 0
for a in A:
    day += 1
    
    cnt += a   
    if day == 7:
        B.append(cnt)
        day = 0   
        cnt = 0
        
print(*B)
