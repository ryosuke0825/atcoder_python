S = input()
YY = int(S[0:2])
MM = int(S[2:4])

if 0 < YY <= 12 and 0 < MM <= 12:
    print("AMBIGUOUS")
elif 0 <= YY <= 99 and 0 < MM <= 12:
    print("YYMM")
elif 0 < YY <= 12 and 0 <= MM <= 99:
    print("MMYY")
else:
	print("NA")
