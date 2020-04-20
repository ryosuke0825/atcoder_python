N = int(input())
A = list(map(int, input().split()))

even = 0
multiple4 = 0
for a in A:
    if a % 4 == 0:
        multiple4 += 1
    elif a % 2 == 0:
        even += 1

N -= ((even//2)*2)+multiple4
if N <= multiple4+1:
    print('Yes')
else:
    print('No')
