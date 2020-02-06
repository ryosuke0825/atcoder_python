s = input()
t = input()

sd = "".join(sorted(s))
td = "".join(sorted(t, reverse=True))

if sd < td:
    print("Yes")
else:
    print("No")
