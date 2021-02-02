A, B = input().split()

sum_a = 0
for a in A:
    sum_a += int(a)

sum_b = 0
for b in B:
    sum_b += int(b)

print(max(sum_a, sum_b))
