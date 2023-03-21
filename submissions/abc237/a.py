N = int(input())
a = 2**31
if N >= -a and N < a:
    print('Yes')
else:
    print('No')
