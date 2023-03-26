N,A,B = map(int,input().split())

ans = (B-A)*(N-2) + 1 if A <= B and N >= B-A else 0
print(ans)
