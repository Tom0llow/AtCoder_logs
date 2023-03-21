import sys


def input():
    return sys.stdin.readline()


def f(a, b):
    return (a + b) * (a ** 2 + b ** 2)


def solve(N):
    max_num = 10 ** 6
    b = max_num
    x = 10 ** 18
    for a in range(max_num + 1):
        while b >= 0 and f(a, b) >= N:
            x = min(x, f(a, b))
            b -= 1
    return x


def main():
    N = int(input())
    ans = solve(N)
    print(ans)


if __name__ == "__main__":
    main()
