N,K = map(int,input().split())

Z = [0]*pow(10,5)
for x in range(pow(10,5)):
    y = sum([int(n) for n in str(x)])
    z = (x+y) % 100000
    Z[x] = z
    

visited = [False]*pow(10,5)
x = Z[N]
ans = []
while True:
    if visited[x]:
        break
    
    visited[x] = True
    ans.append(x)

    x = Z[x]


ind = ans.index(x)
if K <= len(ans):
    print(ans[K-1])
else:
    K -= len(ans)
    ans = ans[ind:]
    print(ans[(K%len(ans)) - 1])
