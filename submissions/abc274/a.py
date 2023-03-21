A,B = map(int,input().split())

S = B/A
S = str(round(S,3))
while len(S)<=4:
    S = S+'0'

print(S)
