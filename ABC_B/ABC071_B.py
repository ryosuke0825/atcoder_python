ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h",
            "i", "j", "k", "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

s = input()
for i in range(26):
    if ALPHABET[i] not in s:
        print(ALPHABET[i])
        break
else:
    print("None")
