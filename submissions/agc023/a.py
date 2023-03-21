from collections import defaultdict

N = int(input())
A = list(map(int,input().split()))

S = [0]*(N+1)
for i in range(N):
    S[i+1] = S[i]+A[i]
nums = defaultdict(int)
for i in range(N+1):
    nums[S[i]] += 1

res = 0
for k,v in nums.items():
    res += v*(v-1) // 2

print(res)

