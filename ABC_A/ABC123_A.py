antenna=[]
for i in range(5):
    antenna.append(int(input()))
k = int(input())

ret = "Yay!"
for i ,coordinate_i in enumerate(antenna):
    for i ,coordinate_j in enumerate(antenna):
        if k < abs(coordinate_i - coordinate_j):
            ret = ":("

print(ret)