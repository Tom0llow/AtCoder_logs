from numpy import double


n = int(input())
a = [int(x) for x in input().split()]
count = 0

while(True):
    even_judge = 0
    
    for v in a:
        if v % 2 == 0:
            even_judge += 1 
    
    if even_judge == n:
        a = list(map(lambda x: x / 2 , a))
        count += 1
    else:
        break

print(count)
