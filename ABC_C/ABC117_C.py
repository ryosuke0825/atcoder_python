N, M = map(int, input().split())
X = list(map(int, input().split()))

if N >= M:
    print(0)
    exit(0)

X.sort()

aida = []
kyori_sum = 0
for i in range(M-1):
    kyori_sum += abs(X[i]-X[i+1])
    aida.append(abs(X[i]-X[i+1]))

aida.sort(reverse=True)
for i in range(N-1):
    kyori_sum -= aida[i]
print(kyori_sum)
