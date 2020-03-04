n = int(input())
B = list(map(int, input().split()))

asum = B[-1]
before_b = B[0]
for i in range(n-1):
    asum += min(B[i], before_b)
    before_b = B[i]

print(asum)
