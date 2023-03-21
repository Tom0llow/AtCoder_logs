S = input()

if len(S) == 1:
    S *= 6
elif len(S) == 2:
    S *= 3
else:
    S *= 2

print(S)
