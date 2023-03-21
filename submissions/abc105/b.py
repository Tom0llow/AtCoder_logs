N = int(input())
ans = 'No'
for cake in range(N+1):
    for donut in range(N+1): 
        if 4 * cake + 7 * donut == N:
            ans = 'Yes'
            break
print(ans)
