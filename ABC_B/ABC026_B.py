import math
n = int(input())

rl = []
for i in range(1, n+1):
    rl.append((int(input())**2))

rl.sort(reverse=True)
red_circle = sum(rl[::2])
white_circle = sum(rl[1::2])
print((red_circle-white_circle)*math.pi)
