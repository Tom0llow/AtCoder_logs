N, Q = map(int, input().split())
S = input()

P = 0
for _ in range(Q):
    q, x = map(int, input().split())
    if q == 1:
        P += x
    else:
        print(S[(x-P)%N-1])
    
