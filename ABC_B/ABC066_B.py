s = input()[:-1]
if len(s) % 2 != 0:
    s = s[:-1]

for i in reversed(range(0, len(s)+2, 2)):
    half = i//2
    if s[:half] == s[half:]:
        print(len(s))
        break
    s = s[:-2]
