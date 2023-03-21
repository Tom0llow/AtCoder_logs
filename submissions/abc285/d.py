from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

strs = defaultdict(str)
seen = defaultdict(int)


N = int(input())
for i in range(N):
    s,t = input().split()
    strs[s] = t
    seen[s] = 1

def dfs(i,target):
    if strs[i] == target:
        print('No')
        exit()
    elif strs[i] in strs and seen[i]:
        seen[i] = 0
        dfs(strs[i],target)


for i in strs.keys():
    dfs(i,i)

print('Yes')
