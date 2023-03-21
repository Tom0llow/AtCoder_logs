N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans1 = 0
for a, b in zip(A, B):
    if a == b:
        ans1 += 1

A, B = set(A), set(B)
ans2 =  len((A & B)) - ans1

print(ans1)
print(ans2)
