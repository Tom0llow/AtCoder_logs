import random

N = int(input())
num_list = [i for i in range(1, 2*N+2)]

while len(num_list) > 0:
    n = random.choice(num_list)
    num_list.remove(n)
    print(n)

    n = int(input())
    if n == 0: break
    else: num_list.remove(n) 



    
