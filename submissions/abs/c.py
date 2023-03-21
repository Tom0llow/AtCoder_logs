n, yen = map(int, input().split())

x, y, z = -1, -1, -1

for x_ in range(n+1):
    for y_ in range(n+1 -x_):
        z_ = n - (x_ + y_)
        if yen == 10000 * x_ + 5000 * y_ + 1000 * z_:
            x, y, z = x_, y_, z_
            break

print(x, y, z)




'''
n, y = (int(x) for x in input().split())
boolean = False

for x_ in range(0, n+1):
    for y_ in range(0, n+1):
        for z_ in range(0, n+1):
            if y == 10000*x_ + 5000*y_ + 1000*z_:  
                if n == x_ + y_ + z_:
                    a_ = x_
                    b_ = y_
                    c_ = z_
                    boolean = True
                    break 
                
if boolean:
    print('{} {} {}'.format(a_, b_, c_)) 
else:
    print('-1 -1 -1')
'''
