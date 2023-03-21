from decimal import Decimal, ROUND_HALF_UP

X,K = map(int,input().split())

Y = Decimal(str(X))
for i in range(1,K+1):
    Y = Y.quantize(Decimal('1E{}'.format(i)), rounding=ROUND_HALF_UP)

ans = int(Y)
print(ans)
