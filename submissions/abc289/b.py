N,M = map(int,input().split())
a = list(map(int,input().split()))

stack = []
ans = []

for i in range(1,N+1):
    stack.append(i)
    while stack and i not in a:
        print(stack.pop())

