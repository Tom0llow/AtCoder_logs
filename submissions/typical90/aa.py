N = int(input())
S = [input() for _ in range(N)]

DB = set()
for i in range(N):
    DBsize = len(DB) 
    DB.add(S[i])
    
    if DBsize < len(DB):
        print(i+1)

    
