ABC = list(map(int, input().split()))
K = int(input())

ABC.sort()
for _ in range(K):
    ABC[2] = ABC[2]*2
print(ABC[0]+ABC[1]+ABC[2])
