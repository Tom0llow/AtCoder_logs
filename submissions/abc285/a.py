a,b = map(int,input().split())

d = {
    1:[2,3],
    2:[4,5],
    3:[6,7],
    4:[8,9],
    5:[10,11],
    6:[12,13],
    7:[14,15]
}    

ans = 'No'
if a in d:
    if b in d[a]:
        ans = 'Yes'

print(ans)
    
