A, B, C, X, Y = map(int, input().split())

#AB�s�U��AB�s�U�𔃂�������S�T�����ĉ���
#AB�s�U��ab���������Ƃ���ƁA
#A�s�U��ab/2�����AB�s�U��ab/2�������邽�߁A����Ȃ��ꍇ�͕ʓr�����悤�ɂ���
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
