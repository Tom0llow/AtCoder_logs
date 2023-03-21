L1, R1, L2, R2 = map(int, input().split())


ans = 0
if L1 <= L2 and R2 <= R1:
    ans = R2-L2
elif L2 <= L1 and R1 <= R2:
    ans = R1-L1
elif L1 <= L2 and R1 >= L2:
        ans = R1-L2
elif L1 >= L2 and L1 <= R2:
    ans = R2-L1

print(ans)
