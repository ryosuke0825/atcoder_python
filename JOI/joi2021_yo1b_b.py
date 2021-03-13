N = int(input())
S = input()

if S.find("I") == -1:
    print("No")
    exit(0)

i = S.find("I")
if S.find("O", i, N) == -1:
    print("No")
    exit(0)

o = S.find("O", i, N)
if S.find("I", o, N) == -1:
    print("No")
    exit(0)

print("Yes")
