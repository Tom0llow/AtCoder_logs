'''
a = int(input())
b = int(input())
c = int(input())

s = input()

total = a + b + c

print(total,' ',s)
'''

#–Í”Í‰ğ“š
a = int(input())

b,c = (int(x) for x in input().split())

s = input()

print("{} {}".format(a+b+c, s))
