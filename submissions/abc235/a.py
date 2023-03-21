a, b, c = (int(x) for x in input())

abc = str(a) + str(b) + str(c)
bca = str(b) + str(c) + str(a)
cab = str(c) + str(a) + str(b)

s = int(abc) + int(bca) + int(cab)
print(s)
