n = int(input())
A = list(map(int, input().split()))

sum_l = sum(A)
sum_r = 0
half_abs = 2020202020
for a in A:
    sum_l -= a
    sum_r += a
    tmp_abs = abs(sum_l-sum_r)
    half_abs = min(half_abs, tmp_abs)
print(half_abs)
