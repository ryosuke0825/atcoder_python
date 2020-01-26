h = int(input())

bin_h = bin(h)
bin_h = bin_h[:2] + bin_h[2:].replace("0", "1")
print(int(bin_h, 2))
