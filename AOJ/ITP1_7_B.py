while True:
    n, x = map(int, input().split())

    if n == 0 and x == 0:
        break

    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            tmp = x-(i+j)
            if i+j+tmp == x and 1 <= tmp <= n:
                if i != j and i != tmp and j != tmp:
                    ans += 1
    print(ans//6)
