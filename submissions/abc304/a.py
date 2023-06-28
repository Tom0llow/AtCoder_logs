N = int(input())

name = []
age = []
for _ in range(N):
    S,A = input().split()
    name.append(S)
    age.append(int(A))


i = age.index(min(age))
name = name[i:] + name[:i] 

print(*name, sep='\n')
