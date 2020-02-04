n = input()

if n.count("3"):
    print("YES")
elif int(n) % 3 == 0:
    print("YES")
else:
    print("NO")
