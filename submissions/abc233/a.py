X, Y = map(int, input().split())
x = X
stamp = 0

while X < Y:
    stamp += 1
    X = x + stamp * 10
    
print(stamp)
