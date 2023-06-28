N = int(input())

if 0 <= N%5 <= 2:
    print(N-N%5)
else:
    print(5*(N//5+1))
