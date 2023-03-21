N, K = map(int, input().split())
S = [int(input()) for _ in range(N)]

for i in range(N):
    if S[i] == 0:   
        print(N)
        exit()

res = 0
right = 0
mul = 1
# print(S)
for left in range(N):
    while right < N and mul*S[right] <= K:
        mul *= S[right]
        right += 1
        # print(S[left:right])
    res = max(res, right-left)

    if right == left:   right += 1 
    else:   mul /= S[left]

print(res)
