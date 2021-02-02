import copy

N = int(input())*2
M = int(input())

deck = [0]*N
for i in range(N):
    deck[i] = i+1

idx = []
for i in range(1, N+1):
    if i % 2 == 0:
        idx.apped(set(, i-1))
    else:
        idx.append(set((i-1)*2, i-1))


for _ in range(M):
    K = int(input())
    new_deck = [0]*N
    if K == 0:
        for i in range(N//2):
            new_deck[i] = deck[i*2]
        for i in range(N//2, N):
            new_deck[i] = deck[i*2]

    deck = copy.deepcopy(new_deck)

for d in deck:
    print(d)
