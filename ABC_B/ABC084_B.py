a, b = map(int, input().split())
s = input()

if s[a] == "-" and s[:a].isdigit() and s[b+1:].isdigit():
    print("Yes")
else:
    print("No")
