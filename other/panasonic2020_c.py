a, b, c = map(int, input().split())

if c-(a+b) > 0 and a*b*4 < (c-a-b)**2:
    print('Yes')
else:
    print('No')
