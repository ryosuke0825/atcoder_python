A, B = map(int, input().split())

# A<=x<y<=B の時に最大公約数cが成り立つかBから見ていく
for c in range(B, 0, -1):
    # A以上B以下のcの倍数の数が2個以上であるか
    if (A+c-1)//c < B//c:
        print(c)
        exit(0)
