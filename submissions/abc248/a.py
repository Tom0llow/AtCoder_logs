S = input()

num_list = list(range(0,10))

for s in S:
    if int(s) in num_list:
        num_list.remove(int(s))

print(num_list.pop(0))
