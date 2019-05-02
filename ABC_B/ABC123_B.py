abcde = []
abcde.append(int(input()))
abcde.append(int(input()))
abcde.append(int(input()))
abcde.append(int(input()))
abcde.append(int(input()))

min_remainder_index = -1
for i in range(len(abcde)):
    remainder = abcde[i] % 10
    if remainder != 0:
        if min_remainder_index == -1:
            min_remainder_index = i
        elif abcde[min_remainder_index] % 10 > remainder:
            min_remainder_index = i

sum = 0
for i in range(len(abcde)):
    if i == min_remainder_index:
        sum += abcde[i]
    elif abcde[i] % 10 == 0:
        sum += abcde[i]
    else:
        sum += abcde[i] + (10-abcde[i] % 10)
print(sum)
