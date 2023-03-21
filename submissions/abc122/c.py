N,Q = map(int,input().split())
string_ = input()

a = [0]*N
for i in range(N):
    if 'AC' == string_[i-1:i+1]:
        a[i] = 1

S = [0]*(N+1)
for i in range(N):
    S[i+1] = S[i]+a[i]

for _ in range(Q):
    l,r = map(int,input().split())
    print(S[r]-S[l])
