S = str(input())

ans = 0
acgt = []
for s in S:
    if s in 'ACGT':
        acgt.append(s)
    else:
        if ans <= len(acgt):
            ans = len(acgt)
        acgt = []       

if ans <= len(acgt):
            ans = len(acgt)
        

print(ans)
