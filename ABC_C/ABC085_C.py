N, Y = map(int, input().split())

for i in range(0, N+1):
    for j in range(0, N+1-i):
        k = N-i-j
        if 1000*i+5000*j+10000*k == Y:
            print(k, j, i)
            exit(0)
print(-1, -1, -1)
