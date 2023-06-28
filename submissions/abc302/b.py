H,W = map(int,input().split())
S = [input() for _ in range(H)]

starts = []
for i in range(H):
    for j in range(W):
        if S[i][j] == 's':
            starts.append([i,j])


def judge_tate(i,j,k):
    for n in range(1,5):
        i += k
        if not 0 <= i < H:    return False
        if S[i][j] != word[n]:  return False
        ans.append([i,j])
    return True

def judge_yoko(i,j,k):
    for n in range(1,5):
        j += k
        if not 0 <= j < W:    return False
        if S[i][j] != word[n]:  return False
        ans.append([i,j])
    return True

def judge_naname1(i,j,k):
    for n in range(1,5):
        i += k
        j += k
        if (not 0 <= i < H) or (not 0 <= j < W):    return False
        if S[i][j] != word[n]:  return False
        ans.append([i,j])
    return True

def judge_naname2(i,j,k):
    for n in range(1,5):
        i += k
        j -= k
        if (not 0 <= i < H) or (not 0 <= j < W):    return False
        if S[i][j] != word[n]:  return False
        ans.append([i,j])
    return True

word = 'snuke'
for i,j in starts:
    ans = [[i,j]]
    if judge_tate(i,j,1):   break
    ans = [[i,j]]
    if judge_tate(i,j,-1):   break

    ans = [[i,j]]
    if judge_yoko(i,j,1):   break
    ans = [[i,j]]
    if judge_yoko(i,j,-1):   break

    ans = [[i,j]]
    if judge_naname1(i,j,1):   break    
    ans = [[i,j]]
    if judge_naname1(i,j,-1):   break

    ans = [[i,j]]
    if judge_naname2(i,j,1):   break    
    ans = [[i,j]]
    if judge_naname2(i,j,-1):   break


for a,b in ans:
    print(a+1,b+1)
