A, B = map(int, input().split())

if (A*B) % 100 == 0:
    print((A*B)//100)
else:
    print((A*B)/100)
