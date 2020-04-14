C = []
for _ in range(3):
    c1, c2, c3 = map(int, input().split())
    tmp = [c1, c2, c3]
    C.append(tmp)

if not(C[0][0]-C[0][1] == C[1][0]-C[1][1] == C[2][0]-C[2][1]):
    print('No')
    exit(0)

if not(C[0][1]-C[0][2] == C[1][1]-C[1][2] == C[2][1]-C[2][2]):
    print('No')
    exit(0)

if not(C[0][0]-C[1][0] == C[0][1]-C[1][1] == C[0][2]-C[1][2]):
    print('No')
    exit(0)

if not(C[1][0]-C[2][0] == C[1][1]-C[2][1] == C[1][2]-C[2][2]):
    print('No')
    exit(0)
print('Yes')
