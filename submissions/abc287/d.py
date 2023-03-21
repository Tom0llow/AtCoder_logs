from collections import defaultdict

def match_or_not(a,b):
    return a=='?' or b=='?' or a==b
    
S = input()
T = input()

pre = defaultdict(bool)
pre[0] = True
for i in range(len(T)):
    if not match_or_not(S[i],T[i]): 
        break
    pre[i+1] = True

suf = defaultdict(bool)
suf[0] = True
for i in range(len(T)):
    if not match_or_not(S[-(i+1)],T[-(i+1)]): 
        break
    suf[i+1] = True

for x in range(len(T)+1):
    if pre[x] and suf[len(T)-x]:
        print('Yes')
    else:
        print('No')
   
