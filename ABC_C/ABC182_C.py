N = input()
M = len(N)

for st in range(M):
    for ed in range(st+1, M-st+1):
        print(N[st:ed])
