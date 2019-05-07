S = list(input())
T = input()

for _ in S:
    S.insert(0, S[-1])
    del S[-1]
    S_str = "".join(S)
    if S_str == T:
        print("Yes")
        exit(0)
print("No")
