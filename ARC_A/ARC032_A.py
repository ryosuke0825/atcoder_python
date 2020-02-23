n = int(input())
nsum = 0
for i in range(1, n+1):
    nsum += i

if nsum == 1:
    print('BOWWOW')
elif nsum <= 3:
    print('WANWAN')
else:
    for i in range(2, n+1):
        if n % i == 0:
            print('BOWWOW')
            break
    else:
        print('WANWAN')
