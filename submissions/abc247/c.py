def S(n):
    if n == 1:  return 1
    else: return [S(n-1), n, S(n-1)]

def number(arr):
    result=[]

    if isinstance(arr, int):
        result.append(arr)

    if isinstance(arr, list):
        for brr in arr:
            result += number(brr)

    return result

N = int(input())
ans = number(S(N)) 

for a in ans:
    print(a)
