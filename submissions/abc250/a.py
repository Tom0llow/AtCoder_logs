H, W = map(int, input().split())
R, C = map(int, input().split())


if H == 1:
    if W == 1:
        print(0)
        exit()
    else:
        if C == 1 or C == W:
            print(1)
            exit()
        else:
            print(2)
            exit()
else:
    if W == 1:
        if R == 1 or R == H:
            print(1)
            exit()
        else:
            print(2)
            exit()


if H == 2:
    if W == 2:
        print(2)
        exit()
    else:
        if C == 1 or C == W:
            print(2)
            exit()
        else:
            print(3)
            exit()
else:
    if W == 2:
        if R == 1 or R == H:
            print(2)
            exit()
        else:
            print(3)
            exit()




if R == 1 or R == H:
    if C == 1 or C == W:
        ans = 2
    else:
        ans = 3
else:
    if C == 1 or C == W:
        ans = 3
    else:
        ans = 4

print(ans)
