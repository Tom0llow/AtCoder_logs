N = int(input())
S = [input() for _ in range(N)]
S.reverse()

print(*S, sep='\n')
