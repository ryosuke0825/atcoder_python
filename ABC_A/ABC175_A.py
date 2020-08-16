S = input()

if S.count('R') != 2:
    print(S.count('R'))
elif S.count('RR') == 1:
    print(2)
else:
    print(1)
