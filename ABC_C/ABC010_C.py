import math

txa, tya, txb, tyb, T, V = map(int, input().split())
n = int(input())
xy = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    xy.append(tmp)

sum_time = T*V
for i in range(n):
    to_house = math.sqrt(((xy[i][0]-txa)**2+(xy[i][1]-tya)**2))
    to_goal = math.sqrt(((xy[i][0]-txb)**2+(xy[i][1]-tyb)**2))
    if sum_time >= to_house+to_goal:
        print('YES')
        exit(0)

print('NO')
