A, B, C, D, E, F, X = map(int, input().split())

def walk_calc(walk_time, rest_time):
    X_curr = X
    _walk = 0
    while X_curr > 0:
        if X_curr >= walk_time: 
            _walk += walk_time
        else:
            _walk += X_curr
        X_curr -= walk_time
        X_curr -= rest_time
    return _walk

T_walk = walk_calc(A, C)            
A_walk = walk_calc(D, F)

T_dist = T_walk * B
A_dist = A_walk * E

if T_dist > A_dist:
    print('Takahashi')
elif T_dist == A_dist:
    print('Draw')
else:
    print('Aoki')
