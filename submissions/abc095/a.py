A, B, C, X, Y = map(int, input().split())

#ABピザがABピザを買う枚数を全探索して解く
#ABピザをab枚買ったとすると、
#Aピザはab/2枚分、Bピザもab/2枚分作れるため、足りない場合は別途買うようにする
ans = 0
if A+B > 2*C:
    ans += 2*C * (min(X,Y))
else:
    ans += (A+B) * (min(X,Y))

if X > Y:
    A_needed = X - Y
    if A > 2*C:
        ans += 2*C * A_needed
    else:
        ans += A * A_needed
else:
    B_needed = Y - X
    if B > 2*C:
        ans += 2*C * B_needed
    else:
        ans += B * B_needed

print(ans)
