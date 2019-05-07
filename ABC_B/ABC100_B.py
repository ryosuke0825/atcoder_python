D, N = map(int, input().split())

if D == 0:
    if N != 100:
        print(N)
    else:
        print(101)
elif D == 1:
    if N != 100:
        print(100*N)
    else:
        print(100*(N+1))
else:
    if N != 100:
        print(10000*N)
    else:
        print(10000*(N+1))
