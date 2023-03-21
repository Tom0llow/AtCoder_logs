N = int(input())

if N >= 42:
    N += 1

if N >= 10:
    ans = 'AGC0' + str(N)
else:
    ans = 'AGC00' + str(N)

print(ans)
