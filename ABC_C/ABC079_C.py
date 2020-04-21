A, B, C, D = list(input())

N = 3
for i in range(2**N):
    op123 = ['+', '+', '+']
    for j in range(N):
        if((i >> j) & 1):
            op123[j] = '-'

    if eval(A+op123[0]+B+op123[1]+C+op123[2]+D) == 7:
        print((A+op123[0]+B+op123[1]+C+op123[2]+D+'=7'))
        exit(0)
