n = int(input())
h = [int(x) for x in input().split()]

box = h[0]

for i in range(1, n):
    if  box < h[i]:
        box = h[i]
    else:
        break

print(box)
