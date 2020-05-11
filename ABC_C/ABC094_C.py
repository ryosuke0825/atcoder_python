N = int(input())
X = list(map(int, input().split()))

xs = sorted(X)
median1 = xs[N//2-1]
median2 = xs[N//2]

for i in range(N):
    if X[i] == median1:
        print(median2)
    elif X[i] == median2:
        print(median1)
    elif X[i] < median1:
        print(median2)
    elif X[i] > median2:
        print(median1)
