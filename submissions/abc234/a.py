t = int(input())

def f(x):
    fx = x**2 + 2 * x + 3
    return fx

answer = f(f(f(t)+t) + f(f(t)))

print(answer)
