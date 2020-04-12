N = int(input())
s_10 = []
s_not_10 = []

for _ in range(N):
    s = int(input())
    if s % 10 == 0:
        s_10.append(s)
    else:
        s_not_10.append(s)

if len(s_not_10) == 0:
    print(0)
    exit(0)

s_not_10_sum = sum(s_not_10)
if s_not_10_sum % 10 != 0:
    print(s_not_10_sum+sum(s_10))
    exit(0)

s_not_10.sort()
print(s_not_10_sum+sum(s_10)-s_not_10[0])
