N = list(input())
N_int = int("".join(N))

NS = 0
for i in N:
    NS += int(i)

if N_int % NS == 0:
    print("Yes")
else:
    print("No")
