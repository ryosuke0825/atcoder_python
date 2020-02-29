n, a, b = map(int, input().split())
S = input()

asum = 0
bsum = 0
for s in S:
    if s == 'a' and asum+bsum < a+b:
        asum += 1
        print('Yes')
    elif s == 'b' and (asum+bsum < a+b and bsum < b):
        bsum += 1
        print('Yes')
    else:
        print('No')
