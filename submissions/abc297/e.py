import heapq

N,K = map(int,input().split())
A = list(map(int,input().split()))

Q = [0]
ans = [0]*(K+1)

for i in range(K+1):
    v = heapq.heappop(Q)
    while i-1 >= 0 and ans[i-1] == v: 
        v = heapq.heappop(Q)
    ans[i] = v
    for ai in A:
        heapq.heappush(Q, v+ai)
    
# print(ans)
print(ans[K])
