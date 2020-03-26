abcd = list(map(int, input()))
a = abcd[0]
b = abcd[1]
c = abcd[2]
d = abcd[3]


if a+b+c+d == 7:
    print(str(a)+'+'+str(b)+'+'+str(c)+'+'+str(d)+'=7')
elif a+b+c-d == 7:
    print(str(a)+'+'+str(b)+'+'+str(c)+'-'+str(d)+'=7')
elif a-b+c+d == 7:
    print(str(a)+'-'+str(b)+'+'+str(c)+'+'+str(d)+'=7')
elif a+b-c+d == 7:
    print(str(a)+'+'+str(b)+'-'+str(c)+'+'+str(d)+'=7')
elif a-b+c-d == 7:
    print(str(a)+'-'+str(b)+'+'+str(c)+'-'+str(d)+'=7')
elif a+b-c-d == 7:
    print(str(a)+'+'+str(b)+'-'+str(c)+'-'+str(d)+'=7')
elif a-b-c+d == 7:
    print(str(a)+'-'+str(b)+'-'+str(c)+'+'+str(d)+'=7')
elif a-b-c-d == 7:
    print(str(a)+'-'+str(b)+'-'+str(c)+'-'+str(d)+'=7')
