N, A, B = map(int, input().split())

ans = []
for i in range(1, N+1):
    lin = ''
    if i % 2 != 0:
        for j in range(1, N+1):
            if j % 2 != 0:
                lin += '.'*B
            else:
                lin += '#'*B
            if j == N:
                lin += '\n'
    
    else:
        for j in range(1, N+1):
            if j % 2 == 0:
                lin += '.'*B
            else:
                lin += '#'*B
            if j == N:
                lin += '\n'
    
    lin *= A
    ans.append(lin)

print(*ans, sep='\n')
