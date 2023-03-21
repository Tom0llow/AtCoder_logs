A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
D = list(map(int,input().split()))

def cross(a,b):
    return a[0]*b[1] - a[1]*b[0]

def sub(a,b):
    return [a[0]-b[0], a[1]-b[1]]

flag = True
if cross(sub(B,A),sub(C,A)) <= 0:
    flag = False
if cross(sub(C,B),sub(D,B)) <= 0:
    flag = False
if cross(sub(D,C),sub(A,C)) <= 0:
    flag = False
if cross(sub(A,D),sub(B,D)) <= 0:
    flag = False

ans = 'Yes' if flag else 'No'
print(ans)
