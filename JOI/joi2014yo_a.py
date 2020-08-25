N = [0]*5
for i in range(5):
    N[i] = int(input())
    if N[i] < 40:
        N[i] = 40

print(sum(N)//5)
