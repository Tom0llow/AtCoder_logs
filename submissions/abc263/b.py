N = int(input())
P = list(map(int, input().split()))

cnt = 0
i = N-1
while True:
    i = P[i-1]-1  
    cnt += 1
    if i == 0:
        break

print(cnt)
  
