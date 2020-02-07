n = list(input())
x = int("".join(n))

sum = 0
for i in n:
    sum += int(i)

if x % sum == 0:
    print("Yes")
else:
    print("No")
