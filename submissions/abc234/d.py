import heapq

N, K = map(int, input().split())
P = list(map(int, input().split()))
q = P[:K]
heapq.heapify(q)
p = heapq.heappop(q)
print(p)
heapq.heappush(q, p)

ans = None

for i in range(K, N):
    p = P[i]
    first = heapq.heappop(q)
    if p > first:
        heapq.heappush(q, p)
        ans = heapq.heappop(q)
    else:
        ans = first
        
    heapq.heappush(q, ans)
    print(ans)
