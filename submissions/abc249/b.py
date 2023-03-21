S = input()

if S.islower():
    print('No')
    exit()

if S.isupper():
    print('No')
    exit()

for c in S:
    if S.count(c) >= 2:
        print('No')
        exit()

print('Yes')
