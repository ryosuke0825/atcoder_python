while True:
    N, K = map(int, input().split())
    if N == K == 0:
        break

    X = list(map(int, input().split()))

    X.sort()
    print(sum(X[:K]))
