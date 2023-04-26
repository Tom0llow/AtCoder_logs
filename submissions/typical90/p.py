INF = float('inf')

N = int(input())
A,B,C = map(int,input().split())

ans = INF
L = 9999
for i in range(L+1):
    if A*i > N: 
        break
    for j in range(L+1):
        if A*i + B*j > N:
            continue    

        if i+j > ans:
            break

        if (N - (A*i + B*j)) % C == 0:
            k = (N - (A*i + B*j)) // C
            ans = min(ans, i+j+k)

print(ans)
