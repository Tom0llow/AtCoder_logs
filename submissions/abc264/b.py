R, C = map(int, input().split())

if R == 1 or R == 15:
    ans = 'black'

elif R == 2 or R == 14:
    ans = 'black' if C in [1,15] else 'white'

elif R == 3 or R == 13:
    ans = 'white' if C in [2,14] else 'black'

elif R == 4 or R == 12:
    ans = 'black' if C in [1,3,13,15] else 'white'

elif R == 5 or R == 11:
    ans = 'white' if C in [2,4,12,14] else 'black'

elif R == 6 or R == 10:
    ans = 'black' if C in [1,3,5,11,13,15] else 'white'

elif R == 7 or R == 9:
    ans = 'white' if C in [2,4,6,10,12,14] else 'black'    

elif R == 8:
    ans = 'black' if C in [1,3,5,7,9,11,13,15] else 'white'    

print(ans)
