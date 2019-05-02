s = list(input())
len = 0
max_len = 0
for str in s:
    if str in ["A", "C", "G", "T"]:
        len += 1
    else:
        if len > max_len:
            max_len = len
        len = 0
else:
    if len > max_len:
        max_len = len
print(max_len)
