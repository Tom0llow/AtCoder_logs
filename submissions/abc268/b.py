import sys


S = input()
T = input()

if len(S) <= len(T):
    if S == T[:len(S)]:
        print('Yes')
        sys.exit()

print('No')
