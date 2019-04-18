k = int(input())
if k % 2 == 0:
    print('{0:.0f}'.format(((k/2)*(k/2))))
else:
    print('{0:.0f}'.format((((k-1)/2)*((k-1)/2)+((k-1)/2))))
