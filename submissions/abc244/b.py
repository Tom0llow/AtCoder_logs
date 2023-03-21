N = int(input())
S = str(input())

def calc_direction(d, x, y):
    if d == 'E':    x += 1
    elif d == 'S':  y -= 1
    elif d == 'W':  x -= 1
    elif d == 'N':  y += 1
    return d, x, y

def judge(d, x, y, t):
    if t == 'S':
        d, x, y = calc_direction(d, x, y)
    elif t == 'R':
        if d == 'E':    d = 'S'
        elif d == 'S':  d = 'W'
        elif d == 'W':  d = 'N'
        elif d == 'N':  d = 'E'
    return d, x, y

d, x, y = 'E', 0, 0
for t in S:
    d, x, y = judge(d, x, y, t)

print(x, y)
