sa = list(input())
sb = list(input())
sc = list(input())

next_turn = "a"
ans = ""
while True:
    if next_turn == "a":
        if len(sa) == 0:
            ans = "A"
            break
        next_turn = sa[0]
        del sa[0]
    elif next_turn == "b":
        if len(sb) == 0:
            ans = "B"
            break
        next_turn = sb[0]
        del sb[0]
    else:
        if len(sc) == 0:
            ans = "C"
            break
        next_turn = sc[0]
        del sc[0]

print(ans)
