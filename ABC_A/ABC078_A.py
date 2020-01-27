hex = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
x, y = input().split()

if hex[x] > hex[y]:
    print(">")
elif hex[x] < hex[y]:
    print("<")
else:
    print("=")
