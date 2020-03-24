import math

n, k = map(int, input().split())
A = list(map(int, input().split()))

mi = min(A)
cnt = A.count(mi)
print(math.ceil((n-cnt)/(k-1)))
