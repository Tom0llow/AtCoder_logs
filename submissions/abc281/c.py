import bisect

def cumsum(xs):
  result = [xs[0]]
  for x in xs[1:]:
    result.append(result[-1] + x)
  return result

N,T = map(int,input().split())
A = list(map(int,input().split()))

cs = cumsum(A)
t = T
if T > cs[-1]:
    t = T%cs[-1]    
q = bisect.bisect_left(cs,t)+1
r = A[q-1] - (cs[q-1]-t)

print(q,r)
