a, b = map(int, input().split())

import numpy
diff = numpy.abs(a-b)
ans = 'No'
if diff == 1 or diff == 9:
    ans = 'Yes'

print(ans)
