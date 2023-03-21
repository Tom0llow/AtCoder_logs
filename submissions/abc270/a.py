A,B = map(int,input().split())

l = set()

if A == 1:
    l.add(1)
elif A == 2:
    l.add(2)
elif A == 3:
    l.add(1)
    l.add(2)
elif A == 4:
    l.add(4)
elif A == 5:
    l.add(1)
    l.add(4)
elif A == 6:
    l.add(2)
    l.add(4)
elif A == 7:
    l.add(1)
    l.add(2)
    l.add(4)


if B == 1:
    l.add(1)
elif B == 2:
    l.add(2)
elif B == 3:
    l.add(1)
    l.add(2)
elif B == 4:
    l.add(4)
elif B == 5:
    l.add(1)
    l.add(4)
elif B == 6:
    l.add(2)
    l.add(4)
elif B == 7:
    l.add(1)
    l.add(2)
    l.add(4)

ans = list(l)
print(sum(ans))
