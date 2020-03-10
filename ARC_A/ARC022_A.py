s = input()

i_index = 101
if s.count('i') >= 1:
    i_index = s.index('i')

I_index = 101
if s.count('I') >= 1:
    I_index = s.index('I')

if i_index == I_index == 101:
    print('NO')
    exit(0)

s = s[min(i_index, I_index)+1:]


c_index = 101
if s.count('c') >= 1:
    c_index = s.index('c')

C_index = 101
if s.count('C') >= 1:
    C_index = s.index('C')

if c_index == C_index == 101:
    print('NO')
    exit(0)

s = s[min(c_index, C_index)+1:]


if s.count('t') >= 1 or s.count('T') >= 1:
    print('YES')
else:
    print('NO')
