N = int(input())
A,B,C = map(int,input().split())

ans = pow(10,18)
for x in range(10000):
    if A*x > N:
        break

    for y in range(10000-x):
        if A*x+B*y > N:
            break
        
        if (N - (A*x+B*y)) % C == 0:
            z = (N - (A*x+B*y)) // C
            ans = min(ans, x+y+z)

print(ans)
