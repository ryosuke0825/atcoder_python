w = input()
wd = list(set(w))

for word in wd:
    if w.count(word) % 2 != 0:
        print("No")
        break
else:
    print("Yes")
