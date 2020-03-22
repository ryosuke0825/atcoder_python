import numpy

n = int(input())
A = list(map(int, input().split()))
res = numpy.cumsum(A)

ans = 10**10
for i in range(n-1):
    ans = min(ans, abs(res[i]-(res[-1]-res[i])))
print(ans)
