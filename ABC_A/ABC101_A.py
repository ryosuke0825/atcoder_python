s = list(input())
ret = 0
for val in s:
    if val == "+":
        ret += 1
    else:
        ret -= 1
print(ret)
