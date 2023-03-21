S = input()

if len(S) < 8:
    print('No')
    exit()

if not (65 <= ord(S[0]) <= 90 and 65 <= ord(S[-1]) <= 90):
    print('No')
    exit()

S = S[1:-1]
n = ''
for s in S:
    if 48 <= ord(s) <= 57:
        n += s
    else:
        print('No')
        exit()

if not (100000 <= int(n) <= int(999999) and len(n) == 6):
    print('No')
    exit()
    
print('Yes')
