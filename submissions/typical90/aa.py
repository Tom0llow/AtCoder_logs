N = int(input())

users = set()
ans = []
for i in range(1,N+1):
    length = len(users)
    
    s = input()
    users.add(s)
    
    if len(users) > length:
        ans.append(i)

    # print(users)

print(*ans, sep='\n')
