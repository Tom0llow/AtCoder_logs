N = int(input())
S = input()

if S.count('T') > S.count('A'): 
    ans = 'T'
elif S.count('T') == S.count('A'):
    ans = 'T' if S[-1] == 'A' else 'A'
else:
    ans = 'A'

print(ans)
