import re
S = input()


if S[0] != "A":
    print("WA")
    exit()

S_3_end2 = S[2:-1]
if S_3_end2.count("C") != 1:
    print("WA")
    exit()

if len(re.findall("[A-Z]", S)) != 2:
    print("WA")
    exit()

print("AC")
