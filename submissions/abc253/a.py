import statistics


a, b, c = map(int, input().split())

l = [a,b,c]
if statistics.median(l) == b:
    print('Yes')
else:
    print('No')
