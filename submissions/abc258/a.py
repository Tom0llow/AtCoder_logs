K = int(input())

if K < 60:
    if K < 10:
        print('21:0{}'.format(K))
    else:
        print('21:{}'.format(K))
else:
    K -= 60
    if K < 10:
        print('22:0{}'.format(K))
    else:
        print('22:{}'.format(K))
