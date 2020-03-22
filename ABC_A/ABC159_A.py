import math

n, m = map(int, input().split())


ans_n = 0
if n <= 1:
    ans_n = 0
else:
    ans_n = math.factorial(n)//(math.factorial(n-2)*math.factorial(2))

ans_m = 0
if m <= 1:
    ans_m = 0
else:
    ans_m = math.factorial(m)//(math.factorial(m-2)*math.factorial(2))
print(ans_n+ans_m)
