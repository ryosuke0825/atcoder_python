n = int(input())
bn = str(bin(n))
bn = "1" + (bn[3:]).replace("1", "0")
print(int(bn, 2))
