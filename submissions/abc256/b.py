N = int(input())
A = list(map(int, input().split()))

P = 0
runners = [0,0,0,0]
for i in range(N): 
    runners[0] = 1
    idx = [x for x, y in enumerate(runners) if y == 1]
    for x in reversed(idx):
        if x + A[i] >= 4:
            P += 1
        else:
            runners[x+A[i]] = 1
        runners[x] = 0

print(P)
