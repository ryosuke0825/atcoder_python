X, K, D = map(int, input().split())

q, r = divmod(X, D)

if abs(X) >= K*D:
    print(abs(X)-K*D)
elif abs(K-q) % 2 == 0:
    print(r)
else:
    print(abs(r-D))
