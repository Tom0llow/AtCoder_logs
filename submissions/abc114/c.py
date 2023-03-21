#abc114c


def DFS(S):
    cnt = 0
    num_list = ['3', '5', '7']
    if len(S) > 0:
        if int(S) > N:
            return cnt
        else:
            flag = True
            for c in num_list:
                if not c in S:
                    flag = False
                    break
            if flag: cnt += 1
    for c in num_list:
        S += c
        cnt += DFS(S)
        S = S[:-1]
    return cnt

N = int(input())
S = ''
ans = DFS(S)
print(ans)
