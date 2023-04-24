from itertools import product

N = int(input())

def judge(A):
    l,r = 0,0
    for a in A:
        if a:   l += 1
        else:   r += 1

        if l < r:
            return False
    
    return l == r

def make_ans(pro):
    S = ''
    for p in pro:
        if p:   S += '('
        else:   S += ')'
    return S


ans = []
for pro in product([0,1], repeat=N):
    if judge(pro):
        S = make_ans(pro)
        ans.append(S)


ans.sort()
print(*ans, sep='\n')

    
