N = int(input())
sum = 0
max_value = 0
for i in range(N):
    tmp = int(input())
    sum += tmp
    max_value = max(max_value, tmp)

print('{0:.0f}'.format(sum - max_value / 2))
