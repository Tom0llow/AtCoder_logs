N = int(input())
S = input()

cnt = 0
stack = []

for s in S:
    stack.append(s)
    if s == '(': 
        cnt += 1
    
    if stack[-1] == ')' and cnt > 0:
        while stack:
            if stack.pop() == '(':
                cnt -= 1
                break

print(''.join(stack))
