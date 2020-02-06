n = int(input())
s = input().split()

arare = 0
if "P" in s:
    arare += 1
if "W" in s:
    arare += 1
if "G" in s:
    arare += 1
if "Y" in s:
    arare += 1

if arare == 3:
    print("Three")
else:
    print("Four")
