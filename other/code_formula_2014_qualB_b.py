N = input()

odd = 0
even = 0
nr = N[::-1]

for i in range(len(N)):
    if (i+1) % 2 != 0:
        odd += int(nr[i])
    else:
        even += int(nr[i])
print(even, odd)
