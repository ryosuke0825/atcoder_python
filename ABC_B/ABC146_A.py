n = int(input())
s = input()

ans = ""
for c in s:
    ord_code = ord(c)
    ord_code += n

    if ord_code > 90:
        ord_code -= 26

    ord_char = chr(ord_code)
    ans += ord_char

print(ans)
