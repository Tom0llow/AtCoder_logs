S = input()
a, b = map(int, input().split())

ans = S[:a-1] + S[b-1] + S[a:b-1] + S[a-1] + S[b:]

print(ans)
'''
ch,o,k,u,dai
01,2,3,4,567
'''
