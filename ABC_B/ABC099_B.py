a, b = map(int, input().split())
c = b-a
sum = 0
for i in range(1, c):
    sum += i
print(sum-a)
