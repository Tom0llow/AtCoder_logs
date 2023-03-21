N = int(input())
A = list(map(int, input().split()))

def ok1(K):
    f, g = 0, 0
    for a in A:
        f, g = g, max(f, g) + a - K
    return max(f, g) > 0

def ok2(K):
    f, g = 0, 0
    for a in A:
        f, g = g, max(f, g) + (1 if a >= K else -1)
    return max(f, g) > 0

x = 0
b = 1e9
while b > 1e-4:
    if ok1(x + b):
        x += b
    b /= 2
print(x)

x = 0
b = 10**9
while b > 0:
    while ok2(x + b):
        x += b
    b //= 2
print(x)
