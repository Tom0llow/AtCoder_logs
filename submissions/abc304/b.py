N = int(input())

if N <= 1000-1:
    print(N)

elif 1000 <= N <= 10000-1:
    print(str(N)[:-1] + '0')

elif 10000 <= N <= 100000-1:
    print(str(N)[:-2] + '00')
    
elif 100000 <= N <= 1000000-1:
    print(str(N)[:-3] + '000')
    
elif 1000000 <= N <= 10000000-1:
    print(str(N)[:-4] + '0000')

elif 10000000 <= N <= 100000000-1:
    print(str(N)[:-5] + '00000')

elif 100000000 <= N <= 1000000000-1:
    print(str(N)[:-6] + '000000')
