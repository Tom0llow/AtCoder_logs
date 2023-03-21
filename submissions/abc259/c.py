def RLE(S):
    cnt = 1
    Run_Length_List = list()
    for i in range(1,len(S)):
        if S[i] == S[i-1]:
            cnt += 1
        else:
            Run_Length_List.append((S[i-1],cnt))
            cnt = 1
    Run_Length_List.append((S[-1],cnt))
    
    return Run_Length_List


S = input()
T = input()

S2 = RLE(S)
T2 = RLE(T)


if len(S2) != len(T2):
    print('No')
    exit()

for i in range(len(S2)):
    if S2[i][0] != T2[i][0]:
        print('No')
        exit()
       
    if S2[i][1] == T2[i][1]:
        continue
    else:
        if S2[i][1] >= 2 and S2[i][1] < T2[i][1]:
            continue
        else:
            print('No')
            exit()

print('Yes')
