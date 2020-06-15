N, L = map(int, input().split())
amida = []
for _ in range(L+1):
    tmp = list(input())
    amida.append(tmp)

idx = amida[L].index('o')
for i in reversed(range(L)):
    if idx != N*2-2 and amida[i][idx+1] == '-':
        idx += 2
    elif idx != 0 and amida[i][idx-1] == '-':
        idx -= 2
print(idx//2+1)
