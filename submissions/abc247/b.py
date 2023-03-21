from collections import defaultdict

N = int(input())
name_dict = defaultdict(int)
name_list = []
for _ in range(N):
    s, t = input().split()
    name_list.append([s,t])
    name_dict[s] += 1
    name_dict[t] += 1
   
    
ans = 'Yes'
for s, t in name_list:
    if s != t:
        if name_dict[s] > 1 and name_dict[t] > 1:
            ans = 'No'
            break
    else:
        if name_dict[s]-2 >= 1 and name_dict[t]-2 >= 1:
            ans = 'No'
            break 
print(ans)
